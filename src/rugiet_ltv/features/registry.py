"""Feature registry: metadata for training and scoring."""

from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum


class FeatureGroup(StrEnum):
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    E = "E"


@dataclass(frozen=True)
class FeatureMeta:
    name: str
    feature_group: FeatureGroup
    lgbm_dtype: str  # "numeric" | "category"
    available_at_first_purchase: bool
    description: str
    group_e_source: str | None = None  # "historical_benchmark" | "sbg_model" | None


def _registry() -> tuple[FeatureMeta, ...]:
    return (
        FeatureMeta("completion_rate", FeatureGroup.A, "numeric", True, "questions answered / total"),
        FeatureMeta("completion_time_seconds", FeatureGroup.A, "numeric", True, "intake duration"),
        FeatureMeta("completion_speed", FeatureGroup.A, "numeric", True, "questions per minute"),
        FeatureMeta("condition_severity_ord", FeatureGroup.A, "numeric", True, "ordinal severity"),
        FeatureMeta("condition_duration_ord", FeatureGroup.A, "numeric", True, "ordinal duration"),
        FeatureMeta("previous_treatment", FeatureGroup.A, "numeric", True, "prior treatment flag"),
        FeatureMeta("previous_treatment_type", FeatureGroup.A, "category", True, "prior treatment type"),
        FeatureMeta("num_health_goals", FeatureGroup.A, "numeric", True, "count of stated goals"),
        FeatureMeta("health_goal_energy", FeatureGroup.A, "numeric", True, "multi-hot goal"),
        FeatureMeta("health_goal_confidence", FeatureGroup.A, "numeric", True, "multi-hot goal"),
        FeatureMeta("health_goal_sleep", FeatureGroup.A, "numeric", True, "multi-hot goal"),
        FeatureMeta("health_goal_weight", FeatureGroup.A, "numeric", True, "multi-hot goal"),
        FeatureMeta("motivation_score", FeatureGroup.A, "numeric", True, "1-10 motivation"),
        FeatureMeta("device_type", FeatureGroup.A, "category", True, "device"),
        FeatureMeta("questionnaire_category", FeatureGroup.A, "category", True, "intake category"),
        FeatureMeta("acquisition_channel", FeatureGroup.B, "category", True, "marketing channel"),
        FeatureMeta("acquisition_campaign", FeatureGroup.B, "category", True, "campaign id"),
        FeatureMeta("acquisition_source", FeatureGroup.B, "category", True, "utm-style source"),
        FeatureMeta("is_referral", FeatureGroup.B, "numeric", True, "referral flag"),
        FeatureMeta("days_from_first_touch_to_purchase", FeatureGroup.B, "numeric", True, "funnel days"),
        FeatureMeta("acquisition_campaign_te", FeatureGroup.B, "numeric", True, "TE campaign", None),
        FeatureMeta("acquisition_source_te", FeatureGroup.B, "numeric", True, "TE source", None),
        FeatureMeta("channel_avg_ltv_te", FeatureGroup.B, "numeric", True, "TE channel", None),
        FeatureMeta("state_avg_ltv_te", FeatureGroup.C, "numeric", True, "TE state", None),
        FeatureMeta("age_bucket", FeatureGroup.C, "category", True, "age band"),
        FeatureMeta("gender", FeatureGroup.C, "category", True, "gender"),
        FeatureMeta("state", FeatureGroup.C, "category", True, "US state"),
        FeatureMeta("state_region", FeatureGroup.C, "category", True, "census region"),
        FeatureMeta("first_product_category", FeatureGroup.D, "category", True, "SKU category at T0"),
        FeatureMeta("first_product_sku", FeatureGroup.D, "category", True, "product SKU"),
        FeatureMeta("first_product_sku_te", FeatureGroup.D, "numeric", True, "TE SKU", None),
        FeatureMeta("subscription_plan", FeatureGroup.D, "category", True, "plan name"),
        FeatureMeta("billing_interval_days", FeatureGroup.D, "numeric", True, "billing cadence days"),
        FeatureMeta("initial_price", FeatureGroup.D, "numeric", True, "first order gross revenue"),
        FeatureMeta("initial_contribution_margin", FeatureGroup.D, "numeric", True, "first order CM sum"),
        FeatureMeta("discount_pct", FeatureGroup.D, "numeric", True, "discount on subscription"),
        FeatureMeta("promo_code_used", FeatureGroup.D, "numeric", True, "discount > 0"),
        FeatureMeta("bundle_flag", FeatureGroup.D, "numeric", True, "multi-SKU first order"),
        FeatureMeta("num_skus_first_order", FeatureGroup.D, "numeric", True, "distinct SKUs at T0"),
        FeatureMeta("payment_method_type", FeatureGroup.D, "category", True, "payment rail"),
        FeatureMeta("auto_refill_enabled", FeatureGroup.D, "numeric", True, "auto refill"),
        FeatureMeta("is_chronic_category", FeatureGroup.D, "numeric", True, "chronic vs episodic cat"),
        FeatureMeta("plan_commitment_months", FeatureGroup.D, "numeric", True, "implied commitment"),
        FeatureMeta(
            "category_cohort_retention_benchmark",
            FeatureGroup.E,
            "numeric",
            True,
            "historical mean 12m LTV for cat x plan",
            "historical_benchmark",
        ),
        FeatureMeta(
            "predicted_p_active_month_12",
            FeatureGroup.E,
            "numeric",
            True,
            "sBG P(active @12m); placeholder in Phase 1",
            "sbg_model",
        ),
        FeatureMeta(
            "predicted_p_active_month_24",
            FeatureGroup.E,
            "numeric",
            True,
            "sBG P(active @24m); placeholder",
            "sbg_model",
        ),
        FeatureMeta(
            "predicted_expected_months_retained",
            FeatureGroup.E,
            "numeric",
            True,
            "sBG expected tenure; placeholder",
            "sbg_model",
        ),
    )


REGISTRY: tuple[FeatureMeta, ...] = _registry()


def load_registry() -> tuple[FeatureMeta, ...]:
    return REGISTRY


def list_feature_names(only_initial_score: bool = True) -> list[str]:
    names = [m.name for m in REGISTRY]
    if only_initial_score:
        names = [m.name for m in REGISTRY if m.available_at_first_purchase]
    return names


def categorical_feature_names() -> list[str]:
    return [m.name for m in REGISTRY if m.lgbm_dtype == "category"]
