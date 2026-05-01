import pandas as pd

from rugiet_ltv.data.synthetic import generate_synthetic_bundle
from rugiet_ltv.features.encoding import FoldTargetEncoders
from rugiet_ltv.features.pipeline import build_feature_matrix, build_raw_feature_table
from rugiet_ltv.features.spine import build_training_spine
from rugiet_ltv.features.targets import compute_ltv_labels
from rugiet_ltv.models.lightgbm_model import LightGBMLTVModel


def test_synthetic_to_lgbm_predict():
    bundle = generate_synthetic_bundle(400, seed=7)
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
    ref = spine_l[["customer_id", "contribution_margin_ltv_12m"]]
    X = build_feature_matrix(
        spine_l,
        bundle.questionnaire_responses,
        bundle.orders,
        encoders=enc,
        label_ref_for_group_e=ref,
        y_train_mean=float(y.mean()),
    )
    feat = [c for c in X.columns if c != "customer_id"]
    m = LightGBMLTVModel(n_estimators=50, learning_rate=0.1)
    m.fit(X[feat], y)
    pred = m.predict_point(X[feat])
    assert len(pred) == len(X)
    assert not pd.isna(pred).any()
