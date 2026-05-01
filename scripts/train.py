#!/usr/bin/env python3
"""Train LightGBM LTV models on synthetic data with temporal backtesting."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import pandas as pd

from rugiet_ltv.data.synthetic import generate_synthetic_bundle
from rugiet_ltv.evaluation.backtest import temporal_backtest_splits
from rugiet_ltv.evaluation.metrics import compute_metrics
from rugiet_ltv.features.encoding import FoldTargetEncoders
from rugiet_ltv.features.pipeline import build_feature_matrix, build_raw_feature_table
from rugiet_ltv.features.spine import build_training_spine
from rugiet_ltv.features.targets import compute_ltv_labels
from rugiet_ltv.models.lightgbm_model import LightGBMLTVModel
from rugiet_ltv.utils.logging import get_logger

log = get_logger(__name__)


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--n-customers", type=int, default=5000)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--output-dir", type=Path, default=Path("artifacts/train_run"))
    p.add_argument("--n-folds", type=int, default=3)
    p.add_argument("--skip-backtest", action="store_true")
    args = p.parse_args()

    bundle = generate_synthetic_bundle(args.n_customers, seed=args.seed)
    spine = build_training_spine(
        bundle.customers,
        bundle.orders,
        bundle.subscriptions,
    )
    labels = compute_ltv_labels(bundle.orders, spine)
    spine_l = spine.merge(labels, on="customer_id", how="inner")

    fold_rows = []
    if not args.skip_backtest:
        for fold in temporal_backtest_splits(spine_l, n_folds=args.n_folds):
            tr = spine_l.loc[fold.train_mask].copy()
            va = spine_l.loc[fold.val_mask].copy()
            if len(tr) < 30 or len(va) < 5:
                continue
            raw_tr = build_raw_feature_table(tr, bundle.questionnaire_responses, bundle.orders)
            y_by_cust = tr.set_index("customer_id")["contribution_margin_ltv_12m"]
            y_tr = raw_tr["customer_id"].map(y_by_cust)
            enc = FoldTargetEncoders.fit(raw_tr.drop(columns=["customer_id"]), y_tr)
            label_ref = tr[["customer_id", "contribution_margin_ltv_12m"]]
            X_tr = build_feature_matrix(
                tr,
                bundle.questionnaire_responses,
                bundle.orders,
                encoders=enc,
                label_ref_for_group_e=label_ref,
                y_train_mean=float(y_tr.mean()),
            )
            X_va = build_feature_matrix(
                va,
                bundle.questionnaire_responses,
                bundle.orders,
                encoders=enc,
                label_ref_for_group_e=label_ref,
                y_train_mean=float(y_tr.mean()),
            )
            y_map = va.set_index("customer_id")["contribution_margin_ltv_12m"]
            y_va = y_map.loc[X_va["customer_id"].values].reset_index(drop=True)

            feat_cols = [c for c in X_tr.columns if c != "customer_id"]
            model = LightGBMLTVModel(n_estimators=200)
            model.fit(X_tr[feat_cols], y_tr, X_val=X_va[feat_cols], y_val=y_va)
            pred = model.predict_point(X_va[feat_cols])
            q = model.predict_quantiles(X_va[feat_cols])
            m = compute_metrics(y_va.to_numpy(), pred, q)
            m["fold"] = fold.fold_id
            fold_rows.append(m)
            log.info("fold %s metrics: %s", fold.fold_id, m)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    if fold_rows:
        metrics_path = args.output_dir / "backtest_metrics.json"
        pd.DataFrame(fold_rows).to_json(metrics_path, orient="records", indent=2)

    raw_all = build_raw_feature_table(spine_l, bundle.questionnaire_responses, bundle.orders)
    y_by_all = spine_l.set_index("customer_id")["contribution_margin_ltv_12m"]
    y_all = raw_all["customer_id"].map(y_by_all)
    enc_full = FoldTargetEncoders.fit(raw_all.drop(columns=["customer_id"]), y_all)
    label_ref_full = spine_l[["customer_id", "contribution_margin_ltv_12m"]]
    X_all = build_feature_matrix(
        spine_l,
        bundle.questionnaire_responses,
        bundle.orders,
        encoders=enc_full,
        label_ref_for_group_e=label_ref_full,
        y_train_mean=float(y_all.mean()),
    )
    feat_cols = [c for c in X_all.columns if c != "customer_id"]
    n = len(X_all)
    val_cut = int(n * 0.85)
    X_trf, X_valf = X_all.iloc[:val_cut], X_all.iloc[val_cut:]
    y_trf = X_trf["customer_id"].map(y_by_all).reset_index(drop=True)
    y_valf = X_valf["customer_id"].map(y_by_all).reset_index(drop=True)
    final = LightGBMLTVModel(n_estimators=300)
    final.fit(X_trf[feat_cols], y_trf, X_val=X_valf[feat_cols], y_val=y_valf)
    bundle_path = args.output_dir / "model_bundle"
    tmax = spine_l["t0"].max()
    final.save_bundle(bundle_path, train_t0_max=tmax)
    meta = {
        "n_customers": args.n_customers,
        "n_rows": n,
        "train_t0_max": tmax.isoformat(),
        "feature_count": len(feat_cols),
    }
    (args.output_dir / "train_meta.json").write_text(json.dumps(meta, indent=2))
    log.info("saved bundle to %s", bundle_path)


if __name__ == "__main__":
    main()
