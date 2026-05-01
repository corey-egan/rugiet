"""Training spine: one row per customer at T0 (first purchase completion)."""

from __future__ import annotations

import pandas as pd


def first_purchase_t0(orders: pd.DataFrame) -> pd.DataFrame:
    """Return customer_id, t0 (first fulfilled_at), first_order_ids as list."""
    o = orders.sort_values(["customer_id", "fulfilled_at", "order_id"])
    first_ts = o.groupby("customer_id")["fulfilled_at"].transform("min")
    first_mask = o["fulfilled_at"] == first_ts
    first_orders = o.loc[first_mask].copy()
    agg = first_orders.groupby("customer_id", as_index=False).agg(
        t0=("fulfilled_at", "first"),
        first_order_ids=("order_id", lambda x: list(x)),
        first_subscription_id=("subscription_id", "first"),
    )
    return agg


def build_training_spine(
    customers: pd.DataFrame,
    orders: pd.DataFrame,
    subscriptions: pd.DataFrame,
) -> pd.DataFrame:
    """Merge customers with T0 and subscription row for the first order's subscription."""
    t0_df = first_purchase_t0(orders)
    spine = customers.merge(t0_df, on="customer_id", how="inner")

    spine = spine.merge(
        subscriptions,
        left_on="first_subscription_id",
        right_on="subscription_id",
        how="left",
        suffixes=("", "_sub"),
    )
    if "customer_id_sub" in spine.columns:
        spine = spine.drop(columns=["customer_id_sub"])
    return spine.reset_index(drop=True)
