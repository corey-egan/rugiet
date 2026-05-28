"""Validate raw tables against Pandera schemas."""

from __future__ import annotations

import pandas as pd
from pandera.errors import SchemaError

from rugiet_ltv.data.schemas import (
    COST_REFERENCE_SCHEMA,
    CUSTOMERS_SCHEMA,
    ENGAGEMENT_EVENTS_SCHEMA,
    ORDERS_SCHEMA,
    QUESTIONNAIRE_RESPONSES_SCHEMA,
    SUBSCRIPTIONS_SCHEMA,
)


def validate_customers(df: pd.DataFrame) -> pd.DataFrame:
    return CUSTOMERS_SCHEMA.validate(df, lazy=True)


def validate_questionnaire(df: pd.DataFrame) -> pd.DataFrame:
    return QUESTIONNAIRE_RESPONSES_SCHEMA.validate(df, lazy=True)


def validate_subscriptions(df: pd.DataFrame) -> pd.DataFrame:
    return SUBSCRIPTIONS_SCHEMA.validate(df, lazy=True)


def validate_orders(df: pd.DataFrame) -> pd.DataFrame:
    return ORDERS_SCHEMA.validate(df, lazy=True)


def validate_engagement(df: pd.DataFrame) -> pd.DataFrame:
    return ENGAGEMENT_EVENTS_SCHEMA.validate(df, lazy=True)


def validate_cost_reference(df: pd.DataFrame) -> pd.DataFrame:
    return COST_REFERENCE_SCHEMA.validate(df, lazy=True)


def validate_all_or_raise(
    customers: pd.DataFrame,
    questionnaire: pd.DataFrame,
    subscriptions: pd.DataFrame,
    orders: pd.DataFrame,
    engagement: pd.DataFrame,
    cost_reference: pd.DataFrame,
) -> None:
    try:
        validate_customers(customers)
        validate_questionnaire(questionnaire)
        validate_subscriptions(subscriptions)
        validate_orders(orders)
        validate_engagement(engagement)
        validate_cost_reference(cost_reference)
    except SchemaError as e:
        raise ValueError(f"Schema validation failed: {e}") from e
