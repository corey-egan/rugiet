import pandas as pd

from rugiet_ltv.evaluation.backtest import temporal_backtest_splits


def test_temporal_splits_disjoint():
    spine = pd.DataFrame(
        {
            "customer_id": [f"c{i}" for i in range(100)],
            "t0": pd.date_range("2023-01-01", periods=100, freq="D"),
        }
    )
    folds = list(temporal_backtest_splits(spine, n_folds=3))
    assert len(folds) >= 1
    for f in folds:
        assert not (f.train_mask & f.val_mask).any()
