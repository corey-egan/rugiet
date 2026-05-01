"""Group C: demographics + state region."""

from __future__ import annotations

import pandas as pd

from rugiet_ltv.utils.constants import US_STATE_TO_REGION


def demographics_features(spine: pd.DataFrame) -> pd.DataFrame:
    s = spine.copy()
    s["state_region"] = s["state"].map(US_STATE_TO_REGION).fillna("South")
    return s[
        [
            "customer_id",
            "age_bucket",
            "gender",
            "state",
            "state_region",
        ]
    ].copy()
