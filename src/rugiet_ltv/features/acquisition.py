"""Group B: acquisition features (raw + funnel velocity)."""

from __future__ import annotations

import pandas as pd


def acquisition_raw(spine: pd.DataFrame) -> pd.DataFrame:
    s = spine.copy()
    s["days_from_first_touch_to_purchase"] = (s["t0"] - s["first_touch_at"]).dt.total_seconds() / 86400.0
    out = s[
        [
            "customer_id",
            "acquisition_channel",
            "acquisition_campaign",
            "acquisition_source",
            "is_referral",
            "days_from_first_touch_to_purchase",
        ]
    ].copy()
    out["is_referral"] = out["is_referral"].astype(bool).astype(int)
    return out
