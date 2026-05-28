"""Fold-safe target encoding (smoothed mean per category, fit on train fold only)."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import cast

import pandas as pd


def _smoothed_means(
    categories: pd.Series,
    y: pd.Series,
    global_mean: float,
    smoothing: float,
) -> pd.Series:
    df = pd.DataFrame({"c": categories.astype(str), "y": y.astype(float)})
    g = df.groupby("c", observed=False)["y"].agg(["mean", "count"])
    num = g["mean"] * g["count"] + smoothing * global_mean
    den = g["count"] + smoothing
    return num / den


@dataclass
class FoldTargetEncoders:
    """Smoothed target encoding maps per column (fit on train only)."""

    global_mean: float
    smoothing: float = 10.0
    campaign: dict[str, float] = field(default_factory=dict)
    source: dict[str, float] = field(default_factory=dict)
    channel: dict[str, float] = field(default_factory=dict)
    state: dict[str, float] = field(default_factory=dict)
    sku: dict[str, float] = field(default_factory=dict)

    @classmethod
    def fit(
        cls,
        X_train: pd.DataFrame,
        y_train: pd.Series,
        *,
        smoothing: float = 10.0,
    ) -> FoldTargetEncoders:
        gm = float(y_train.mean())
        self = cls(global_mean=gm, smoothing=smoothing)
        self.campaign = cast(
            dict[str, float],
            _smoothed_means(X_train["acquisition_campaign"], y_train, gm, smoothing).to_dict(),
        )
        self.source = cast(
            dict[str, float],
            _smoothed_means(X_train["acquisition_source"], y_train, gm, smoothing).to_dict(),
        )
        self.channel = cast(
            dict[str, float],
            _smoothed_means(X_train["acquisition_channel"], y_train, gm, smoothing).to_dict(),
        )
        self.state = cast(
            dict[str, float],
            _smoothed_means(X_train["state"], y_train, gm, smoothing).to_dict(),
        )
        self.sku = cast(
            dict[str, float],
            _smoothed_means(X_train["first_product_sku"], y_train, gm, smoothing).to_dict(),
        )
        return self

    def _map(self, m: dict[str, float], s: pd.Series) -> pd.Series:
        return s.astype(str).map(m).fillna(self.global_mean)

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        out = X.copy()
        out["acquisition_campaign_te"] = self._map(self.campaign, out["acquisition_campaign"])
        out["acquisition_source_te"] = self._map(self.source, out["acquisition_source"])
        out["channel_avg_ltv_te"] = self._map(self.channel, out["acquisition_channel"])
        out["state_avg_ltv_te"] = self._map(self.state, out["state"])
        out["first_product_sku_te"] = self._map(self.sku, out["first_product_sku"])
        return out


def apply_fold_encoders(
    X: pd.DataFrame,
    encoders: FoldTargetEncoders | None,
    y_mean: float,
) -> pd.DataFrame:
    if encoders is None:
        out = X.copy()
        for c in [
            "acquisition_campaign_te",
            "acquisition_source_te",
            "channel_avg_ltv_te",
            "state_avg_ltv_te",
            "first_product_sku_te",
        ]:
            out[c] = y_mean
        return out
    return encoders.transform(X)
