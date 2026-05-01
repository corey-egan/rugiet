"""Assemble feature matrix from raw tables."""

from __future__ import annotations

import pandas as pd

from rugiet_ltv.features.acquisition import acquisition_raw
from rugiet_ltv.features.demographics import demographics_features
from rugiet_ltv.features.encoding import FoldTargetEncoders, apply_fold_encoders
from rugiet_ltv.features.intake import intake_features
from rugiet_ltv.features.purchase import purchase_features
from rugiet_ltv.features.registry import list_feature_names
from rugiet_ltv.features.survival import compute_interim_group_e


def build_raw_feature_table(
    spine: pd.DataFrame,
    questionnaire: pd.DataFrame,
    orders: pd.DataFrame,
) -> pd.DataFrame:
    """A–D raw columns (no target encoding, no group E)."""
    a = intake_features(spine, questionnaire)
    b = acquisition_raw(spine)
    c = demographics_features(spine)
    d = purchase_features(spine, orders)
    return a.merge(b, on="customer_id").merge(c, on="customer_id").merge(d, on="customer_id")


def build_feature_matrix(
    spine: pd.DataFrame,
    questionnaire: pd.DataFrame,
    orders: pd.DataFrame,
    *,
    encoders: FoldTargetEncoders | None = None,
    label_ref_for_group_e: pd.DataFrame | None = None,
    y_train_mean: float | None = None,
) -> pd.DataFrame:
    """
    Point-in-time features at T0. Target encodings applied via encoders (fit on train fold)
    or filled with y_train_mean when encoders is None.
    """
    x = build_raw_feature_table(spine, questionnaire, orders)

    y_mean = y_train_mean if y_train_mean is not None else 0.0
    x = apply_fold_encoders(x, encoders, y_mean)

    labels_for_e = label_ref_for_group_e
    if labels_for_e is not None and "contribution_margin_ltv_12m" not in labels_for_e.columns:
        labels_for_e = None
    e = compute_interim_group_e(spine, labels_for_e)
    x = x.merge(e, on="customer_id", how="left")

    cols = ["customer_id"] + list_feature_names(only_initial_score=True)
    missing = [c for c in cols if c not in x.columns]
    if missing:
        raise ValueError(f"Missing feature columns: {missing}")
    return x[cols].copy()
