# rugiet

Predictive LTV (contribution margin) at first purchase for Rugiet subscription customers.

Canonical product and modeling plan: [docs/RUGIET_LTV_IMPLEMENTATION_PLAN.md](docs/RUGIET_LTV_IMPLEMENTATION_PLAN.md).

## Quick start

```bash
make install
make lint
make test
python3 scripts/train.py --n-customers 2000 --output-dir artifacts/run1
python3 scripts/evaluate.py --bundle artifacts/run1/model_bundle
```

Package code lives under `src/rugiet_ltv/`.
