# Rugiet LTV Prediction Model - Implementation Plan (Revised)

## Context

Rugiet sells prescription medications across 5 categories (ED, hair loss, weight, TRT, sleep) via a subscription model. We are building a predictive LTV model that scores customers at the **moment of first purchase completion**, using the full set of available signals at that point:

1. **Intake / questionnaire data** - health conditions, severity, duration, previous treatments, motivation, health goals, device, completion patterns
2. **Acquisition data** - channel, campaign, source, referral
3. **Demographics** - age bucket, gender, state
4. **Purchase selection** - product category, specific SKU, subscription plan/cadence, price point, discount, bundle vs single, payment method

### Scale (updated)

- **500K total customers** (historical); **170K active subscribers**
- **30K new customers / month**; **70K orders / month**
- Plenty of volume for ML from day one -- we can skip the "small-data" probabilistic-only baseline

### Goals

1. Score every customer at first purchase with a predicted 6/12-month contribution-margin LTV plus uncertainty band
2. Run retroactively on all 500K historical customers to generate a scored customer file
3. Identify which data points are most/least predictive via SHAP + permutation + group ablation
4. Productionize a real-time scoring API that fires on first-purchase events

---

## Revised Modeling Approach

Because we have 500K customers, we **skip the probabilistic-only baseline phase** and go straight to a gradient-boosted ML model. Probabilistic survival modeling is still valuable, but as a **feature generator** (survival probability fed into the ML model), not a standalone scoring system.

### Primary Model: LightGBM + SHAP

- **Target**: 12-month contribution margin LTV (primary), 24-month LTV (secondary)
- **Features**: All intake/questionnaire + acquisition + demographics + first-purchase selection features
- **Feature importance**: SHAP TreeExplainer for global + per-customer explanations
- **Uncertainty**: Quantile regression (fit 3 LightGBM models at q=0.1, 0.5, 0.9) or bootstrapped ensemble
- **Why LightGBM over XGBoost**: native categorical support for state/campaign/SKU (high cardinality), faster training on 500K rows

### Secondary Model: ZILN Neural Network (Phase 3 comparison)

- Google's Zero-Inflated Lognormal neural network -- now viable at our scale
- Handles heavy-tailed LTV distribution (small % of customers drive most value)
- Handles churned/zero-LTV customers elegantly via the zero-inflation component
- Used as a challenger to LightGBM; keep whichever wins

### Supporting Model: sBG Survival (as a feature)

- PyMC-Marketing Shifted-Beta-Geometric model trained on historical retention curves by segment
- Outputs: predicted P(active at month 12), P(active at month 24), expected months retained
- Fed as features into LightGBM rather than used standalone

### Deferred

| Approach | Why Deferred |
|---|---|
| LSTM/RNN on event sequences | Adds complexity; revisit if Phase 3 ZILN underperforms or for LTV-update model |
| Kuaishou MDME | Billion-user scale; unnecessary at 500K |
| `lifetimes` BG/NBD | Wrong model class for subscription business |

---

## Feature Set (Available at First-Purchase Moment)

All 5 groups below are available when the first order completes. This is a much richer feature set than questionnaire-time scoring.

### Group A: Intake / Questionnaire Features
- `completion_rate` = questions_answered / questions_total
- `completion_time_seconds`, `completion_speed` (questions per minute)
- `condition_severity` (ordinal: mild/moderate/severe)
- `condition_duration` (ordinal: <6mo, 6-12mo, 1-3yr, 3+yr)
- `previous_treatment` (bool), `previous_treatment_type` (categorical)
- `num_health_goals`, `health_goals_encoded` (multi-hot)
- `motivation_score` (1-10)
- `device_type` (mobile/desktop/tablet)
- `questionnaire_category` (ed/hair/weight/trt/sleep)

### Group B: Acquisition Features
- `acquisition_channel` (paid_search, organic, social, podcast, tv, affiliate, referral)
- `acquisition_campaign` (target-encoded; 100s of values)
- `acquisition_source` (google/facebook/tiktok/etc.)
- `is_referral` (bool)
- `channel_avg_ltv` (target-encoded from training fold only)
- `source_avg_ltv` (target-encoded)
- `days_from_first_touch_to_purchase` (funnel velocity)

### Group C: Demographic Features
- `age_bucket` (18-24, 25-34, 35-44, 45-54, 55-64, 65+)
- `gender`
- `state` + `state_region` (Northeast/South/Midwest/West)
- `state_avg_ltv` (target-encoded)

### Group D: Purchase & Plan Selection Features (NEW - critical)
- `first_product_category` (ed/hair/weight/trt/sleep)
- `first_product_sku` (target-encoded if high cardinality)
- `subscription_plan` (monthly/quarterly/annual/6-month)
- `billing_interval_days` (30/60/90/180/365)
- `initial_price` (gross price of first order)
- `initial_contribution_margin` (revenue - cogs - shipping - processing)
- `discount_pct` (promo applied)
- `promo_code_used` (bool + encoded value)
- `bundle_flag` (bought multiple products at once)
- `num_skus_first_order` (bundle size)
- `payment_method_type` (card/apple_pay/google_pay/bnpl)
- `auto_refill_enabled` (bool)
- `is_chronic_category` (ed/hair/trt = chronic; weight/sleep = episodic)
- `plan_commitment_months` (1 for monthly, 3 for quarterly, 12 for annual)

### Group E: Derived Survival Features (from sBG model)
- `predicted_p_active_month_12`
- `predicted_p_active_month_24`
- `predicted_expected_months_retained`
- `category_cohort_retention_benchmark` (historical retention for this category/plan combo)

**Phase 1 note:** Until Phase 2 sBG is wired, only `category_cohort_retention_benchmark` (and optional simple cohort stats) are populated from historical aggregates at T0; `predicted_*` columns are placeholders for Phase 2.

### Post-Purchase Update Features (for LTV refresh models, not initial scoring)
These are used for rescoring existing customers as they accumulate tenure:
- RFM (recency, frequency, monetary), support contacts, reorder velocity, cross-category interest, referrals sent, num active subscriptions

---

## Data Requirements (6 Tables)

User sources these in HIPAA-compliant environment.

1. **`customers`** - de-identified customer dimension (id, created_at, acquisition_*, age_bucket, gender, state, first_product_category, is_active, churn_date)
2. **`questionnaire_responses`** - intake responses (severity, duration, previous_treatment, health_goals, motivation_score, device, completion metrics) - **contains PHI**
3. **`subscriptions`** - subscription lifecycle (subscription_id, customer_id, product_category, product_sku, started_at, cancelled_at, billing_interval_days, monthly_price, discount_pct, cancellation_reason)
4. **`orders`** - fulfilled orders with contribution margin components (revenue, cogs, shipping_cost, payment_processing_fee, refund_amount)
5. **`engagement_events`** - behavioral events for post-purchase LTV updates
6. **`cost_reference`** - product cost dimension (unit_cogs, fulfillment_cost, avg_payment_processing_pct)

**Target variable**: `contribution_margin_ltv_12m(customer) = SUM(contribution_margin)` over orders within 12 months of first purchase, where `contribution_margin = revenue - cogs - shipping_cost - payment_processing_fee - refund_amount`.

---

## Project Structure

```
rugiet/
├── pyproject.toml
├── Makefile
├── .gitignore
├── README.md
├── conf/                          # YAML configs
├── notebooks/                     # Numbered exploration notebooks
├── src/rugiet_ltv/
│   ├── data/                      # schemas (pandera), loaders, validators, synthetic generators
│   ├── features/                  # intake, acquisition, demographic, purchase, survival, pipeline, registry
│   ├── models/
│   │   ├── base.py                # Abstract BaseLTVModel
│   │   ├── lightgbm_model.py      # Primary LTV predictor (point + quantile)
│   │   ├── survival/              # sBG feature generator
│   │   └── ziln/                  # ZILN challenger (Phase 3)
│   ├── evaluation/                # metrics, backtesting, comparison, reports
│   ├── explainability/            # shap, permutation, group_ablation, feature_report
│   ├── serving/                   # FastAPI app, routes, model_registry, HIPAA middleware
│   └── utils/                     # logging, config, constants
├── tests/
├── scripts/                       # train.py, evaluate.py, score_batch.py, feature_importance.py
└── docker/
```

---

## Roadmap (Compressed for Scale)

### Phase 0: Foundation (Week 1) -- STARTING NOW
- `pyproject.toml` with deps (lightgbm, shap, pandera, pydantic, pymc-marketing, fastapi, optuna, mlflow, sklearn, pandas)
- Directory structure
- Pandera schemas for all 6 tables
- Synthetic data generators producing realistic 500K-customer datasets
- Lint/typecheck/test tooling (ruff, mypy, pytest)

### Phase 1: Feature Pipeline + LightGBM Baseline (Weeks 2-4)
- All 5 feature groups (A-E) computed with point-in-time correctness (E interim in Phase 1 per doc above)
- Feature registry with `available_at_first_purchase: bool` tags
- LightGBM model (point + quantile for uncertainty)
- Temporal backtesting framework
- End-to-end: synthetic data → features → LightGBM → evaluated predictions

### Phase 2: sBG Survival Features + Feature Importance (Weeks 5-6)
- sBG model trained per category/plan segment via PyMC-Marketing
- Survival features fed into LightGBM (Group E)
- SHAP + permutation + group ablation analyses
- Feature importance report identifying most/least predictive signals

### Phase 3: ZILN Challenger + Model Selection (Weeks 7-8)
- ZILN neural net implementation
- Head-to-head comparison with LightGBM on holdout
- Keep winner (or ensemble if close)

### Phase 4: Retroactive Batch Scoring (Week 9)
- `scripts/score_batch.py` to score all 500K historical customers
- Output: scored customer file with customer_id, predicted_ltv_12m, uncertainty band, tier, top factors
- Validation against known outcomes for mature cohorts

### Phase 5: Production API (Weeks 10-12)
- FastAPI `/v1/score` endpoint triggered on first-purchase event
- Model registry with versioning and hot-reload
- HIPAA audit middleware
- Docker, integration tests, load testing (p99 <100ms)

### Phase 6: Real Data + Go-Live (Weeks 13+)
- Ingest real data (user-led, HIPAA-compliant)
- Retrain on real data; recalibrate
- Deploy; set up monthly retraining (easy with 30K/month fresh labels)
- Monitor drift

---

## Verification

1. Unit tests for all feature computations and model fit/predict
2. Integration test: synthetic data → full pipeline → API response
3. Temporal backtesting showing stable performance across cohorts
4. SHAP ↔ permutation importance cross-validation
5. API load test: p99 < 100ms
6. Retroactive scoring sanity check: predicted LTV rank correlation with actual LTV on mature cohorts > 0.6
