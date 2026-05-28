"""LightGBM point + quantile models for 12m contribution margin LTV."""

from __future__ import annotations

import json
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path
from typing import Any, cast

import joblib
import numpy as np
import pandas as pd
from lightgbm import LGBMRegressor, early_stopping, log_evaluation

from rugiet_ltv.features.registry import categorical_feature_names
from rugiet_ltv.models.base import BaseLTVModel


def _cat_cols_present(X: pd.DataFrame) -> list[str]:
    return [c for c in categorical_feature_names() if c in X.columns]


def _prepare_X(X: pd.DataFrame) -> pd.DataFrame:
    out = X.copy()
    for c in _cat_cols_present(out):
        out[c] = out[c].astype("category")
    return out


@dataclass
class LightGBMLTVBundle:
    """Serialized model artifacts (metadata + joblib estimators)."""

    feature_names: list[str]
    categorical_features: list[str]
    point_params: dict[str, Any]
    quantile_params: dict[str, dict[str, Any]]
    train_t0_max: str | None = None

    def save_meta(self, directory: Path) -> None:
        d = Path(directory)
        d.mkdir(parents=True, exist_ok=True)
        meta = {
            "feature_names": self.feature_names,
            "categorical_features": self.categorical_features,
            "point_params": self.point_params,
            "quantile_params": self.quantile_params,
            "train_t0_max": self.train_t0_max,
        }
        (d / "bundle_meta.json").write_text(json.dumps(meta, indent=2))

    @classmethod
    def load_meta(cls, directory: Path) -> LightGBMLTVBundle:
        raw = json.loads((Path(directory) / "bundle_meta.json").read_text())
        return cls(
            feature_names=raw["feature_names"],
            categorical_features=raw["categorical_features"],
            point_params=raw["point_params"],
            quantile_params=raw["quantile_params"],
            train_t0_max=raw.get("train_t0_max"),
        )


class LightGBMLTVModel(BaseLTVModel):
    """Point (L2) + three quantile regressors."""

    def __init__(
        self,
        *,
        random_state: int = 42,
        n_estimators: int = 300,
        learning_rate: float = 0.05,
    ) -> None:
        self.random_state = random_state
        self.n_estimators = n_estimators
        self.learning_rate = learning_rate
        self._point: LGBMRegressor | None = None
        self._quantiles: dict[float, LGBMRegressor] = {}
        self._feature_names: list[str] | None = None
        self._categorical_features: list[str] | None = None

    def fit(
        self,
        X: pd.DataFrame,
        y: pd.Series,
        *,
        X_val: pd.DataFrame | None = None,
        y_val: pd.Series | None = None,
    ) -> None:
        self._feature_names = list(X.columns)
        self._categorical_features = _cat_cols_present(X)
        X_tr = _prepare_X(X)
        cols_list = list(X_tr.columns)
        cat_idx: list[int] = [cols_list.index(c) for c in self._categorical_features]

        callbacks: list[Callable[..., Any]] | None = None
        eval_set = None
        if X_val is not None and y_val is not None:
            X_va = _prepare_X(X_val)
            eval_set = [(X_va, y_val)]
            callbacks = [
                early_stopping(stopping_rounds=30, first_metric_only=True, verbose=False),
                log_evaluation(period=0),
            ]

        self._point = LGBMRegressor(
            objective="regression",
            n_estimators=self.n_estimators,
            learning_rate=self.learning_rate,
            random_state=self.random_state,
            verbosity=-1,
        )
        self._point.fit(
            X_tr,
            y,
            eval_set=cast(Any, eval_set),
            callbacks=callbacks,
            categorical_feature=cat_idx if cat_idx else "auto",
        )

        self._quantiles = {}
        for alpha in (0.1, 0.5, 0.9):
            m = LGBMRegressor(
                objective="quantile",
                alpha=alpha,
                n_estimators=self.n_estimators,
                learning_rate=self.learning_rate,
                random_state=self.random_state,
                verbosity=-1,
            )
            m.fit(
                X_tr,
                y,
                categorical_feature=cat_idx if cat_idx else "auto",
            )
            self._quantiles[alpha] = m

    def predict_point(self, X: pd.DataFrame) -> np.ndarray:
        assert self._point is not None
        assert self._feature_names is not None
        Xp = _prepare_X(X[self._feature_names])
        return cast(np.ndarray, self._point.predict(Xp))

    def predict_quantiles(self, X: pd.DataFrame) -> dict[str, np.ndarray]:
        assert self._feature_names is not None
        Xp = _prepare_X(X[self._feature_names])
        return {f"q{int(a * 100)}": self._quantiles[a].predict(Xp) for a in sorted(self._quantiles)}

    def predict(self, X: pd.DataFrame) -> np.ndarray:
        return self.predict_point(X)

    def save_bundle(
        self,
        directory: Path,
        train_t0_max: pd.Timestamp | None = None,
    ) -> LightGBMLTVBundle:
        assert self._point is not None
        d = Path(directory)
        d.mkdir(parents=True, exist_ok=True)
        joblib.dump(self._point, d / "lgbm_point.joblib")
        for a, m in self._quantiles.items():
            joblib.dump(m, d / f"lgbm_q{int(a * 100)}.joblib")

        def _jsonable_params(m: LGBMRegressor) -> dict[str, Any]:
            p = m.get_params()
            allowed = (str, int, float, bool, type(None))
            return {k: v for k, v in p.items() if isinstance(v, allowed)}

        q_params = {str(a): _jsonable_params(m) for a, m in self._quantiles.items()}
        bundle = LightGBMLTVBundle(
            feature_names=self._feature_names or [],
            categorical_features=self._categorical_features or [],
            point_params=_jsonable_params(self._point),
            quantile_params=q_params,
            train_t0_max=train_t0_max.isoformat() if train_t0_max is not None else None,
        )
        bundle.save_meta(d)
        return bundle

    @classmethod
    def load_bundle(cls, directory: Path) -> tuple[LightGBMLTVModel, LightGBMLTVBundle]:
        d = Path(directory)
        bundle = LightGBMLTVBundle.load_meta(d)
        m = cls()
        m._feature_names = bundle.feature_names
        m._categorical_features = bundle.categorical_features
        m._point = joblib.load(d / "lgbm_point.joblib")
        m._quantiles = {}
        for a_str in bundle.quantile_params:
            alpha = float(a_str)
            m._quantiles[alpha] = joblib.load(d / f"lgbm_q{int(alpha * 100)}.joblib")
        return m, bundle
