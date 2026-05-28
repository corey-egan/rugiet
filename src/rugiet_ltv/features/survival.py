"""Group E: interim cohort benchmark (Phase 1); sBG placeholders for Phase 2."""

from __future__ import annotations

import pandas as pd


def compute_interim_group_e(
    spine: pd.DataFrame,
    labels_reference: pd.DataFrame | None,
) -> pd.DataFrame:
    """
    category_cohort_retention_benchmark: leave-one-out mean 12m LTV within
    (first_product_category, billing_interval_days) using only rows in
    labels_reference, so a customer's benchmark does not include their own label.
    """
    key_cols = ["first_product_category", "billing_interval_days"]
    base = spine[["customer_id"] + key_cols].copy()

    if labels_reference is None or labels_reference.empty:
        return base.assign(
            category_cohort_retention_benchmark=0.0,
            predicted_p_active_month_12=0.5,
            predicted_p_active_month_24=0.35,
            predicted_expected_months_retained=6.0,
        )

    ref = base.merge(
        labels_reference[["customer_id", "contribution_margin_ltv_12m"]],
        on="customer_id",
        how="inner",
    )
    global_mean = float(ref["contribution_margin_ltv_12m"].mean())

    g = ref.groupby(key_cols, as_index=False).agg(
        _sum=("contribution_margin_ltv_12m", "sum"),
        _cnt=("contribution_margin_ltv_12m", "count"),
    )
    merged = ref.merge(g, on=key_cols, how="left")
    merged["category_cohort_retention_benchmark"] = global_mean
    m = merged["_cnt"] > 1
    merged.loc[m, "category_cohort_retention_benchmark"] = (
        merged.loc[m, "_sum"] - merged.loc[m, "contribution_margin_ltv_12m"]
    ) / (merged.loc[m, "_cnt"] - 1)
    merged.loc[~m, "category_cohort_retention_benchmark"] = global_mean

    out = base.merge(
        merged[["customer_id", "category_cohort_retention_benchmark"]],
        on="customer_id",
        how="left",
    )
    out["category_cohort_retention_benchmark"] = out["category_cohort_retention_benchmark"].fillna(global_mean)

    out["predicted_p_active_month_12"] = 0.5
    out["predicted_p_active_month_24"] = 0.35
    out["predicted_expected_months_retained"] = 6.0
    return out[
        [
            "customer_id",
            "category_cohort_retention_benchmark",
            "predicted_p_active_month_12",
            "predicted_p_active_month_24",
            "predicted_expected_months_retained",
        ]
    ]
