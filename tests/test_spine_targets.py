import pandas as pd

from rugiet_ltv.features.spine import build_training_spine, first_purchase_t0
from rugiet_ltv.features.targets import compute_ltv_labels, order_contribution_margin


def test_first_purchase_t0_and_labels():
    orders = pd.DataFrame(
        {
            "order_id": ["o1", "o2", "o3"],
            "customer_id": ["a", "a", "a"],
            "subscription_id": ["s1", "s1", "s1"],
            "fulfilled_at": pd.to_datetime(["2024-01-10", "2024-02-10", "2024-03-10"]),
            "product_sku": ["x", "x", "x"],
            "revenue": [100.0, 50.0, 50.0],
            "cogs": [20.0, 10.0, 10.0],
            "shipping_cost": [5.0, 0.0, 0.0],
            "payment_processing_fee": [3.0, 2.0, 2.0],
            "refund_amount": [0.0, 0.0, 0.0],
        }
    )
    t0 = first_purchase_t0(orders)
    assert t0.loc[t0["customer_id"] == "a", "t0"].iloc[0] == pd.Timestamp("2024-01-10")

    customers = pd.DataFrame(
        {
            "customer_id": ["a"],
            "created_at": pd.to_datetime(["2024-01-01"]),
            "first_touch_at": pd.to_datetime(["2023-12-20"]),
            "acquisition_channel": ["organic"],
            "acquisition_campaign": ["c1"],
            "acquisition_source": ["direct"],
            "is_referral": [False],
            "age_bucket": ["25-34"],
            "gender": ["M"],
            "state": ["TX"],
            "first_product_category": ["ed"],
            "is_active": [True],
            "churn_date": [None],
        }
    )
    subs = pd.DataFrame(
        {
            "subscription_id": ["s1"],
            "customer_id": ["a"],
            "product_category": ["ed"],
            "product_sku": ["x"],
            "started_at": pd.to_datetime(["2024-01-09"]),
            "cancelled_at": [None],
            "billing_interval_days": [30],
            "monthly_price": [99.0],
            "discount_pct": [0.0],
            "cancellation_reason": [None],
            "auto_refill_enabled": [True],
        }
    )
    spine = build_training_spine(customers, orders, subs)
    labels = compute_ltv_labels(orders, spine)
    # All three orders within 12m of T0
    cm = order_contribution_margin(orders)
    expected = float(cm.sum())
    got = labels.loc[labels["customer_id"] == "a", "contribution_margin_ltv_12m"].iloc[0]
    assert abs(got - expected) < 1e-6


def test_questionnaire_before_t0():
    from rugiet_ltv.features.intake import attach_questionnaire_at_t0

    spine = pd.DataFrame(
        {
            "customer_id": ["x"],
            "t0": pd.to_datetime(["2024-06-01"]),
        }
    )
    q = pd.DataFrame(
        {
            "response_id": ["1", "2"],
            "customer_id": ["x", "x"],
            "completed_at": pd.to_datetime(["2024-05-01", "2024-05-20"]),
            "questions_total": [10, 10],
            "questions_answered": [8, 10],
            "completion_time_seconds": [300.0, 200.0],
            "condition_severity": ["mild", "severe"],
            "condition_duration": ["<6mo", "1-3yr"],
            "previous_treatment": [False, True],
            "previous_treatment_type": [None, "rx"],
            "health_goals": ["energy", "energy,confidence"],
            "motivation_score": [5, 8],
            "device_type": ["mobile", "desktop"],
            "questionnaire_category": ["ed", "ed"],
        }
    )
    picked = attach_questionnaire_at_t0(spine, q)
    assert len(picked) == 1
    assert picked["completed_at"].iloc[0] == pd.Timestamp("2024-05-20")
