"""Regression and quantile metrics."""

from __future__ import annotations

from typing import Any

import numpy as np
import pandas as pd


def mae(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    return float(np.mean(np.abs(y_true - y_pred)))


def rmse(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    return float(np.sqrt(np.mean((y_true - y_pred) ** 2)))


def mape(y_true: np.ndarray, y_pred: np.ndarray, eps: float = 1e-8) -> float:
    denom = np.maximum(np.abs(y_true), eps)
    return float(np.mean(np.abs((y_true - y_pred) / denom)) * 100.0)


def spearman(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    r = pd.Series(y_true).corr(pd.Series(y_pred), method="spearman")
    return float(r) if r == r else 0.0  # NaN check


def pinball_loss(y_true: np.ndarray, y_pred: np.ndarray, quantile: float) -> float:
    e = y_true - y_pred
    return float(np.mean(np.maximum(quantile * e, (quantile - 1) * e)))


def interval_coverage(y_true: np.ndarray, q_low: np.ndarray, q_high: np.ndarray) -> float:
    return float(np.mean((y_true >= q_low) & (y_true <= q_high)))


def compute_metrics(
    y_true: np.ndarray,
    y_point: np.ndarray,
    quantiles: dict[str, np.ndarray] | None = None,
) -> dict[str, Any]:
    out: dict[str, Any] = {
        "mae": mae(y_true, y_point),
        "rmse": rmse(y_true, y_point),
        "mape": mape(y_true, y_point),
        "spearman": spearman(y_true, y_point),
    }
    if quantiles:
        q10 = quantiles.get("q10")
        q50 = quantiles.get("q50")
        q90 = quantiles.get("q90")
        if q10 is not None:
            out["pinball_q10"] = pinball_loss(y_true, q10, 0.1)
        if q50 is not None:
            out["pinball_q50"] = pinball_loss(y_true, q50, 0.5)
        if q90 is not None:
            out["pinball_q90"] = pinball_loss(y_true, q90, 0.9)
        if q10 is not None and q90 is not None:
            out["interval_q10_q90_coverage"] = interval_coverage(y_true, q10, q90)
    return out


def metrics_to_frame(rows: list[dict[str, Any]]) -> pd.DataFrame:
    return pd.DataFrame(rows)
