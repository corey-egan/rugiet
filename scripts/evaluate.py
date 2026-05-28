#!/usr/bin/env python3
"""Evaluate a saved LightGBM bundle on a synthetic holdout."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from rugiet_ltv.data.synthetic import generate_synthetic_bundle
from rugiet_ltv.evaluation.metrics import compute_metrics
from rugiet_ltv.features.encoding import FoldTargetEncoders
from rugiet_ltv.features.pipeline import build_feature_matrix, build_raw_feature_table
from rugiet_ltv.features.spine import build_training_spine
from rugiet_ltv.features.targets import compute_ltv_labels
from rugiet_ltv.models.lightgbm_model import LightGBMLTVModel


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--bundle", type=Path, required=True)
    p.add_argument("--n-customers", type=int, default=1500)
    p.add_argument("--seed", type=int, default=99)
    p.add_argument("--output", type=Path, default=None)
    args = p.parse_args()

    bundle = generate_synthetic_bundle(args.n_customers, seed=args.seed)
    spine = build_training_spine(
        bundle.customers,
        bundle.orders,
        bundle.subscriptions,
    )
    labels = compute_ltv_labels(bundle.orders, spine)
    spine_l = spine.merge(labels, on="customer_id", how="inner")

    raw = build_raw_feature_table(spine_l, bundle.questionnaire_responses, bundle.orders)
    y_by = spine_l.set_index("customer_id")["contribution_margin_ltv_12m"]
    y = raw["customer_id"].map(y_by)
    enc = FoldTargetEncoders.fit(raw.drop(columns=["customer_id"]), y)
    label_ref = spine_l[["customer_id", "contribution_margin_ltv_12m"]]
    X = build_feature_matrix(
        spine_l,
        bundle.questionnaire_responses,
        bundle.orders,
        encoders=enc,
        label_ref_for_group_e=label_ref,
        y_train_mean=float(y.mean()),
    )
    feat_cols = [c for c in X.columns if c != "customer_id"]

    model, _bundle = LightGBMLTVModel.load_bundle(args.bundle)
    pred = model.predict_point(X[feat_cols])
    q = model.predict_quantiles(X[feat_cols])
    m = compute_metrics(y.to_numpy(), pred, q)
    out = json.dumps(m, indent=2)
    print(out)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(out)


if __name__ == "__main__":
    main()
