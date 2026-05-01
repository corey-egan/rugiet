"""Pandera schemas for the six core tables."""

from pandera import Check, Column, DataFrameSchema

CUSTOMERS_SCHEMA = DataFrameSchema(
    {
        "customer_id": Column(str, unique=True),
        "created_at": Column("datetime64[ns]"),
        "first_touch_at": Column("datetime64[ns]"),
        "acquisition_channel": Column(str),
        "acquisition_campaign": Column(str),
        "acquisition_source": Column(str),
        "is_referral": Column(bool),
        "age_bucket": Column(str),
        "gender": Column(str),
        "state": Column(str, Check.str_length(2, 2)),
        "first_product_category": Column(str),
        "is_active": Column(bool),
        "churn_date": Column("datetime64[ns]", nullable=True),
    },
    strict=True,
    coerce=True,
)

QUESTIONNAIRE_RESPONSES_SCHEMA = DataFrameSchema(
    {
        "response_id": Column(str, unique=True),
        "customer_id": Column(str),
        "completed_at": Column("datetime64[ns]"),
        "questions_total": Column(int, Check.ge(1)),
        "questions_answered": Column(int, Check.ge(0)),
        "completion_time_seconds": Column(float, Check.ge(0)),
        "condition_severity": Column(str),
        "condition_duration": Column(str),
        "previous_treatment": Column(bool),
        "previous_treatment_type": Column(str, nullable=True),
        "health_goals": Column(str),
        "motivation_score": Column(int, Check.in_range(1, 10)),
        "device_type": Column(str),
        "questionnaire_category": Column(str),
    },
    strict=True,
    coerce=True,
)

SUBSCRIPTIONS_SCHEMA = DataFrameSchema(
    {
        "subscription_id": Column(str, unique=True),
        "customer_id": Column(str),
        "product_category": Column(str),
        "product_sku": Column(str),
        "started_at": Column("datetime64[ns]"),
        "cancelled_at": Column("datetime64[ns]", nullable=True),
        "billing_interval_days": Column(int, Check.isin([30, 60, 90, 180, 365])),
        "monthly_price": Column(float, Check.ge(0)),
        "discount_pct": Column(float, Check.in_range(0, 100)),
        "cancellation_reason": Column(str, nullable=True),
        "auto_refill_enabled": Column(bool),
    },
    strict=True,
    coerce=True,
)

ORDERS_SCHEMA = DataFrameSchema(
    {
        "order_id": Column(str, unique=True),
        "customer_id": Column(str),
        "subscription_id": Column(str, nullable=True),
        "fulfilled_at": Column("datetime64[ns]"),
        "product_sku": Column(str),
        "revenue": Column(float, Check.ge(0)),
        "cogs": Column(float, Check.ge(0)),
        "shipping_cost": Column(float, Check.ge(0)),
        "payment_processing_fee": Column(float, Check.ge(0)),
        "refund_amount": Column(float, Check.ge(0)),
    },
    strict=True,
    coerce=True,
)

ENGAGEMENT_EVENTS_SCHEMA = DataFrameSchema(
    {
        "event_id": Column(str, unique=True),
        "customer_id": Column(str),
        "event_type": Column(str),
        "occurred_at": Column("datetime64[ns]"),
        "metadata_json": Column(str, nullable=True),
    },
    strict=True,
    coerce=True,
)

COST_REFERENCE_SCHEMA = DataFrameSchema(
    {
        "product_sku": Column(str, unique=True),
        "unit_cogs": Column(float, Check.ge(0)),
        "fulfillment_cost": Column(float, Check.ge(0)),
        "avg_payment_processing_pct": Column(float, Check.in_range(0, 100)),
    },
    strict=True,
    coerce=True,
)
