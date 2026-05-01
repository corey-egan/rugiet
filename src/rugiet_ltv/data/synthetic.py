"""Synthetic data generators for development and tests."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Literal

import numpy as np
import pandas as pd

from rugiet_ltv.data.validators import validate_all_or_raise
from rugiet_ltv.utils.constants import (
    ACQUISITION_CHANNELS,
    AGE_BUCKETS,
    CATEGORIES,
    US_STATE_TO_REGION,
)

RNG = np.random.default_rng

Severities = Literal["mild", "moderate", "severe"]
Durations = Literal["<6mo", "6-12mo", "1-3yr", "3+yr"]
Devices = Literal["mobile", "desktop", "tablet"]
Plans = Literal["monthly", "quarterly", "annual", "6-month"]
ACQUISITION_SOURCES = ("google", "facebook", "tiktok", "bing", "direct")
PaymentTypes = Literal["card", "apple_pay", "google_pay", "bnpl"]


@dataclass(frozen=True)
class SyntheticDataBundle:
    customers: pd.DataFrame
    questionnaire_responses: pd.DataFrame
    subscriptions: pd.DataFrame
    orders: pd.DataFrame
    engagement_events: pd.DataFrame
    cost_reference: pd.DataFrame

    def validate(self) -> None:
        validate_all_or_raise(
            self.customers,
            self.questionnaire_responses,
            self.subscriptions,
            self.orders,
            self.engagement_events,
            self.cost_reference,
        )


def _states(rng: np.random.Generator) -> list[str]:
    return list(US_STATE_TO_REGION.keys())


def generate_synthetic_bundle(
    n_customers: int,
    *,
    seed: int = 42,
    avg_orders_after_first: float = 4.0,
    sku_count: int = 80,
    campaign_count: int = 120,
) -> SyntheticDataBundle:
    """Generate a coherent multi-table dataset (suitable for CI at small n, stress at large n)."""
    rng = RNG(seed)
    states = _states(rng)
    skus = [f"SKU-{i:04d}" for i in range(sku_count)]
    campaigns = [f"cmp_{i:04d}" for i in range(campaign_count)]

    customer_ids = [f"cust_{i:08d}" for i in range(n_customers)]

    # Stagger cohorts over ~24 months
    base = pd.Timestamp("2022-01-01", tz="UTC").tz_localize(None)
    offsets_days = rng.integers(0, 730, size=n_customers)
    created = base + pd.to_timedelta(offsets_days, unit="D")
    first_touch = created - pd.to_timedelta(rng.integers(0, 14, size=n_customers).astype("int64"), unit="D")

    cats = list(CATEGORIES)
    channels = list(ACQUISITION_CHANNELS)

    customers_rows = []
    for i, cid in enumerate(customer_ids):
        cat = cats[rng.integers(0, len(cats))]
        customers_rows.append(
            {
                "customer_id": cid,
                "created_at": created[i],
                "first_touch_at": first_touch[i],
                "acquisition_channel": channels[rng.integers(0, len(channels))],
                "acquisition_campaign": campaigns[rng.integers(0, len(campaigns))],
                "acquisition_source": ACQUISITION_SOURCES[rng.integers(0, len(ACQUISITION_SOURCES))],
                "is_referral": bool(rng.random() < 0.08),
                "age_bucket": AGE_BUCKETS[rng.integers(0, len(AGE_BUCKETS))],
                "gender": "M" if rng.random() < 0.72 else "F",
                "state": states[rng.integers(0, len(states))],
                "first_product_category": cat,
                "is_active": bool(rng.random() < 0.55),
                "churn_date": None
                if rng.random() < 0.55
                else (created[i] + pd.to_timedelta(int(rng.integers(30, 400)), unit="D")),
            }
        )
    customers = pd.DataFrame(customers_rows)

    q_rows = []
    for i, cid in enumerate(customer_ids):
        cat = customers.loc[customers["customer_id"] == cid, "first_product_category"].iloc[0]
        qt = 18
        qa = int(rng.integers(12, qt + 1))
        t0_approx = created[i] + pd.to_timedelta(int(rng.integers(1, 5)), unit="D")
        q_rows.append(
            {
                "response_id": f"qr_{i:08d}",
                "customer_id": cid,
                "completed_at": t0_approx - pd.to_timedelta(int(rng.integers(1, 48)), unit="h"),
                "questions_total": qt,
                "questions_answered": qa,
                "completion_time_seconds": float(rng.integers(120, 900)),
                "condition_severity": ["mild", "moderate", "severe"][rng.integers(0, 3)],
                "condition_duration": ["<6mo", "6-12mo", "1-3yr", "3+yr"][rng.integers(0, 4)],
                "previous_treatment": bool(rng.random() < 0.35),
                "previous_treatment_type": None
                if rng.random() < 0.5
                else ["rx", "otc", "lifestyle"][rng.integers(0, 3)],
                "health_goals": ",".join(
                    rng.choice(["energy", "confidence", "sleep", "weight"], size=rng.integers(1, 4))
                ),
                "motivation_score": int(rng.integers(3, 11)),
                "device_type": ["mobile", "desktop", "tablet"][rng.integers(0, 3)],
                "questionnaire_category": cat,
            }
        )
    questionnaire = pd.DataFrame(q_rows)

    sub_rows: list[dict[str, Any]] = []
    order_rows: list[dict[str, Any]] = []
    oid = 0
    billing_choices = [30, 90, 180, 365]

    for i, cid in enumerate(customer_ids):
        cat = customers.loc[customers["customer_id"] == cid, "first_product_category"].iloc[0]
        sku = skus[rng.integers(0, len(skus))]
        sub_id = f"sub_{i:08d}"
        t0 = created[i] + pd.to_timedelta(int(rng.integers(1, 6)), unit="D")
        bill = int(rng.choice(billing_choices))
        sub_rows.append(
            {
                "subscription_id": sub_id,
                "customer_id": cid,
                "product_category": cat,
                "product_sku": sku,
                "started_at": t0,
                "cancelled_at": None
                if rng.random() < 0.5
                else (t0 + pd.to_timedelta(int(rng.integers(60, 500)), unit="D")),
                "billing_interval_days": bill,
                "monthly_price": float(rng.uniform(29, 199)),
                "discount_pct": float(rng.choice([0, 0, 5, 10, 15, 20])),
                "cancellation_reason": None if rng.random() < 0.6 else ["price", "effect", "other"][rng.integers(0, 3)],
                "auto_refill_enabled": bool(rng.random() < 0.85),
            }
        )

        n_extra = max(0, int(rng.poisson(avg_orders_after_first)))
        n_order = 1 + n_extra
        bundle_first = rng.random() < 0.12
        for k in range(n_order):
            fulfilled = t0 + pd.to_timedelta(int(30 * k + rng.integers(0, 5)), unit="D")
            rev = float(rng.uniform(40, 250))
            cogs = rev * float(rng.uniform(0.15, 0.45))
            ship = float(rng.uniform(0, 12))
            proc = rev * float(rng.uniform(0.02, 0.04))
            refund = float(rng.uniform(0, 5)) if rng.random() < 0.05 else 0.0
            if k == 0:
                primary_sku = skus[0] if bundle_first else sku
            else:
                primary_sku = skus[rng.integers(0, len(skus))]
            order_rows.append(
                {
                    "order_id": f"ord_{oid:09d}",
                    "customer_id": cid,
                    "subscription_id": sub_id,
                    "fulfilled_at": fulfilled,
                    "product_sku": primary_sku,
                    "revenue": rev,
                    "cogs": cogs,
                    "shipping_cost": ship,
                    "payment_processing_fee": proc,
                    "refund_amount": refund,
                }
            )
            oid += 1
            if k == 0 and bundle_first:
                order_rows.append(
                    {
                        "order_id": f"ord_{oid:09d}",
                        "customer_id": cid,
                        "subscription_id": sub_id,
                        "fulfilled_at": fulfilled,
                        "product_sku": skus[1],
                        "revenue": float(rng.uniform(20, 80)),
                        "cogs": float(rng.uniform(5, 30)),
                        "shipping_cost": 0.0,
                        "payment_processing_fee": float(rng.uniform(1, 4)),
                        "refund_amount": 0.0,
                    }
                )
                oid += 1

    subscriptions = pd.DataFrame(sub_rows)
    orders = pd.DataFrame(order_rows)

    eng_rows = []
    n_eng = min(n_customers * 3, max(10, n_customers // 10))
    cust_idx = rng.integers(0, n_customers, size=n_eng)
    for i in range(n_eng):
        j = int(cust_idx[i])
        cid = customer_ids[j]
        eng_rows.append(
            {
                "event_id": f"evt_{i:09d}",
                "customer_id": cid,
                "event_type": ["page_view", "email_open", "click"][rng.integers(0, 3)],
                "occurred_at": created[j] + pd.to_timedelta(int(rng.integers(1, 200)), unit="D"),
                "metadata_json": "{}",
            }
        )
    engagement = pd.DataFrame(eng_rows)

    cost_rows = []
    for s in skus:
        cost_rows.append(
            {
                "product_sku": s,
                "unit_cogs": float(rng.uniform(8, 40)),
                "fulfillment_cost": float(rng.uniform(2, 9)),
                "avg_payment_processing_pct": float(rng.uniform(2.0, 3.5)),
            }
        )
    cost_reference = pd.DataFrame(cost_rows)

    bundle = SyntheticDataBundle(
        customers=customers,
        questionnaire_responses=questionnaire,
        subscriptions=subscriptions,
        orders=orders,
        engagement_events=engagement,
        cost_reference=cost_reference,
    )
    bundle.validate()
    return bundle
