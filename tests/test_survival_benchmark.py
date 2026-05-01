import pandas as pd

from rugiet_ltv.features.survival import compute_interim_group_e


def test_loo_benchmark_excludes_self():
    spine = pd.DataFrame(
        {
            "customer_id": ["a", "b", "c"],
            "first_product_category": ["ed", "ed", "hair"],
            "billing_interval_days": [30, 30, 30],
        }
    )
    labels = pd.DataFrame(
        {
            "customer_id": ["a", "b", "c"],
            "contribution_margin_ltv_12m": [100.0, 200.0, 50.0],
        }
    )
    out = compute_interim_group_e(spine, labels)
    # ed/30 cohort: a sees mean of b only -> 200; b sees mean of a only -> 100
    row_a = out.loc[out["customer_id"] == "a", "category_cohort_retention_benchmark"].iloc[0]
    row_b = out.loc[out["customer_id"] == "b", "category_cohort_retention_benchmark"].iloc[0]
    assert abs(row_a - 200.0) < 1e-6
    assert abs(row_b - 100.0) < 1e-6
