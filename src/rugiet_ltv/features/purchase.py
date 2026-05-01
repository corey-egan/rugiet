"""Group D: first-purchase / plan features at T0."""

from __future__ import annotations

import pandas as pd

from rugiet_ltv.features.spine import first_purchase_t0
from rugiet_ltv.features.targets import order_contribution_margin
from rugiet_ltv.utils.constants import CHRONIC_CATEGORIES

BILLING_TO_PLAN = {
    30: "monthly",
    90: "quarterly",
    180: "6-month",
    365: "annual",
}
BILLING_TO_COMMITMENT = {30: 1, 90: 3, 180: 6, 365: 12}


def purchase_features(spine: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    """Derive first-purchase selection from orders at T0 and subscription fields on spine."""
    t0_info = first_purchase_t0(orders)
    o = orders.merge(t0_info[["customer_id", "t0"]], on="customer_id")
    at_t0 = o.loc[o["fulfilled_at"] == o["t0"]].copy()
    at_t0["cm"] = order_contribution_margin(at_t0)

    agg = at_t0.groupby("customer_id", as_index=False).agg(
        initial_price=("revenue", "sum"),
        initial_contribution_margin=("cm", "sum"),
        num_skus_first_order=("product_sku", "nunique"),
        first_product_sku=("product_sku", lambda s: s.iloc[0]),
    )
    agg["bundle_flag"] = (agg["num_skus_first_order"] > 1).astype(int)

    base = spine.merge(agg, on="customer_id", how="left")

    bill = base["billing_interval_days"].fillna(30).astype(int)
    base["subscription_plan"] = bill.map(BILLING_TO_PLAN).fillna("monthly")
    base["billing_interval_days"] = bill
    bic = BILLING_TO_COMMITMENT
    base["plan_commitment_months"] = base["billing_interval_days"].map(bic).fillna(1)

    has_fpc = "first_product_category" in base.columns
    cat_col = "first_product_category" if has_fpc else "product_category"
    base["first_product_category"] = base[cat_col].fillna("ed").astype(str).str.lower()
    chronic = base["first_product_category"].isin(CHRONIC_CATEGORIES)
    base["is_chronic_category"] = chronic.astype(int)

    base["discount_pct"] = base["discount_pct"].fillna(0.0)
    base["promo_code_used"] = (base["discount_pct"] > 0).astype(int)
    base["payment_method_type"] = "card"
    base["auto_refill_enabled"] = base["auto_refill_enabled"].fillna(True).astype(bool).astype(int)

    base["initial_price"] = base["initial_price"].fillna(0.0)
    base["initial_contribution_margin"] = base["initial_contribution_margin"].fillna(0.0)
    base["num_skus_first_order"] = base["num_skus_first_order"].fillna(1).astype(int)

    return base[
        [
            "customer_id",
            "first_product_category",
            "first_product_sku",
            "subscription_plan",
            "billing_interval_days",
            "initial_price",
            "initial_contribution_margin",
            "discount_pct",
            "promo_code_used",
            "bundle_flag",
            "num_skus_first_order",
            "payment_method_type",
            "auto_refill_enabled",
            "is_chronic_category",
            "plan_commitment_months",
        ]
    ].copy()
