"""Group A: questionnaire / intake features at T0."""

from __future__ import annotations

import pandas as pd

from rugiet_ltv.utils.constants import DURATION_ORDER, HEALTH_GOAL_LABELS, SEVERITY_ORDER


def attach_questionnaire_at_t0(spine: pd.DataFrame, questionnaire: pd.DataFrame) -> pd.DataFrame:
    """Latest questionnaire completed on or before T0 per customer."""
    q = questionnaire.copy()
    merged = spine[["customer_id", "t0"]].merge(q, on="customer_id", how="left")
    merged = merged.loc[merged["completed_at"] <= merged["t0"]]
    merged = merged.sort_values(["customer_id", "completed_at"])
    return merged.drop_duplicates(subset=["customer_id"], keep="last")


def intake_features(spine: pd.DataFrame, questionnaire: pd.DataFrame) -> pd.DataFrame:
    q = attach_questionnaire_at_t0(spine, questionnaire)
    out = spine[["customer_id"]].merge(q, on="customer_id", how="left", suffixes=("", "_q"))

    out["completion_rate"] = out["questions_answered"] / out["questions_total"].clip(lower=1)
    out["completion_speed"] = out["questions_answered"] / (out["completion_time_seconds"].clip(lower=1) / 60.0)
    out["condition_severity_ord"] = out["condition_severity"].map(SEVERITY_ORDER).fillna(1)
    out["condition_duration_ord"] = out["condition_duration"].map(DURATION_ORDER).fillna(1)
    out["previous_treatment"] = out["previous_treatment"].fillna(False).astype(bool).astype(int)
    hg_str = out["health_goals"].astype(str).replace({"nan": ""})
    hg = hg_str.str.split(",").str.strip()
    out["num_health_goals"] = hg.apply(lambda xs: len([x for x in (xs if isinstance(xs, list) else []) if x]))
    out["motivation_score"] = out["motivation_score"].fillna(5)
    out["device_type"] = out["device_type"].fillna("mobile")
    out["questionnaire_category"] = out["questionnaire_category"].fillna("ed")

    out["previous_treatment_type"] = out["previous_treatment_type"].fillna("none")

    hg_lower = hg_str.str.lower()
    for g in HEALTH_GOAL_LABELS:
        out[f"health_goal_{g}"] = hg_lower.str.contains(g, regex=False).astype(int)

    cols_a = [
        "customer_id",
        "completion_rate",
        "completion_time_seconds",
        "completion_speed",
        "condition_severity_ord",
        "condition_duration_ord",
        "previous_treatment",
        "previous_treatment_type",
        "num_health_goals",
        *[f"health_goal_{g}" for g in HEALTH_GOAL_LABELS],
        "motivation_score",
        "device_type",
        "questionnaire_category",
    ]
    return out[cols_a].fillna(
        {
            "completion_rate": 0.5,
            "completion_time_seconds": 300.0,
            "completion_speed": 1.0,
        }
    )
