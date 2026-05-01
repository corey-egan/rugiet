"""Label construction: contribution margin LTV over fixed windows after T0."""

from __future__ import annotations

import pandas as pd


def order_contribution_margin(df: pd.DataFrame) -> pd.Series:
    return df["revenue"] - df["cogs"] - df["shipping_cost"] - df["payment_processing_fee"] - df["refund_amount"]


def compute_ltv_labels(
    orders: pd.DataFrame,
    spine: pd.DataFrame,
    *,
    months_12: int = 12,
    months_24: int = 24,
) -> pd.DataFrame:
    """
    For each customer in spine, sum contribution margin on orders with
    fulfilled_at in (T0, T0 + window] (strictly after first purchase for label
    definition clarity; first-order margin at T0 is excluded from *post-first* LTV
    extension — the plan sums orders within 12 months of first purchase; we
    include orders with fulfilled_at > T0 and <= T0+12m, which excludes the
    instant first order at T0 from the 12m sum if T0 equals first fulfilled_at.
    Adjust to include first order if product wants total 12m including first:
    use fulfilled_at >= T0.
    """
    o = orders.merge(spine[["customer_id", "t0"]], on="customer_id", how="inner")
    o = o.assign(cm=order_contribution_margin(o))
    o["dt"] = o["fulfilled_at"] - o["t0"]
    # Include first purchase order in LTV window (typical LTV definition)
    mask_12 = (o["fulfilled_at"] >= o["t0"]) & (o["fulfilled_at"] <= o["t0"] + pd.DateOffset(months=months_12))
    mask_24 = (o["fulfilled_at"] >= o["t0"]) & (o["fulfilled_at"] <= o["t0"] + pd.DateOffset(months=months_24))
    l12 = o.loc[mask_12].groupby("customer_id")["cm"].sum().rename("contribution_margin_ltv_12m")
    l24 = o.loc[mask_24].groupby("customer_id")["cm"].sum().rename("contribution_margin_ltv_24m")
    out = spine[["customer_id"]].merge(l12, on="customer_id", how="left")
    out = out.merge(l24, on="customer_id", how="left")
    out["contribution_margin_ltv_12m"] = out["contribution_margin_ltv_12m"].fillna(0.0)
    out["contribution_margin_ltv_24m"] = out["contribution_margin_ltv_24m"].fillna(0.0)
    return out
