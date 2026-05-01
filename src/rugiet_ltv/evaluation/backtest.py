"""Temporal rolling-origin splits on T0."""

from __future__ import annotations

from collections.abc import Iterator
from dataclasses import dataclass

import pandas as pd


@dataclass(frozen=True)
class TemporalFold:
    fold_id: int
    train_mask: pd.Series
    val_mask: pd.Series


def temporal_backtest_splits(
    spine: pd.DataFrame,
    *,
    n_folds: int = 3,
) -> Iterator[TemporalFold]:
    """
    Quantile-based time slices on t0: train on customers with t0 <= Q(fold),
    validate on (Q(fold), Q(fold+1)].
    """
    t0 = spine["t0"]
    for k in range(n_folds):
        q_lo = (k + 1) / (n_folds + 2)
        q_hi = (k + 2) / (n_folds + 2)
        lo_t = t0.quantile(q_lo)
        hi_t = t0.quantile(q_hi)
        train_mask = t0 <= lo_t
        val_mask = (t0 > lo_t) & (t0 <= hi_t)
        if val_mask.sum() < 2:
            continue
        yield TemporalFold(k, train_mask, val_mask)
