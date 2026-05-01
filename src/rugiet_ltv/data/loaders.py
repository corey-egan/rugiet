"""Load validated tables from Parquet/CSV (stubs for Phase 6)."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from rugiet_ltv.data.validators import validate_all_or_raise


def load_bundle_from_parquet(directory: Path) -> tuple[pd.DataFrame, ...]:
    d = Path(directory)
    customers = pd.read_parquet(d / "customers.parquet")
    questionnaire = pd.read_parquet(d / "questionnaire_responses.parquet")
    subscriptions = pd.read_parquet(d / "subscriptions.parquet")
    orders = pd.read_parquet(d / "orders.parquet")
    engagement = pd.read_parquet(d / "engagement_events.parquet")
    cost_reference = pd.read_parquet(d / "cost_reference.parquet")
    validate_all_or_raise(customers, questionnaire, subscriptions, orders, engagement, cost_reference)
    return customers, questionnaire, subscriptions, orders, engagement, cost_reference
