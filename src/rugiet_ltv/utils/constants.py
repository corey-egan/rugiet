"""Shared constants for categories, regions, and enums."""

CATEGORIES = ("ed", "hair", "weight", "trt", "sleep")
CHRONIC_CATEGORIES = frozenset({"ed", "hair", "trt"})

HEALTH_GOAL_LABELS = ("energy", "confidence", "sleep", "weight")

ACQUISITION_CHANNELS = (
    "paid_search",
    "organic",
    "social",
    "podcast",
    "tv",
    "affiliate",
    "referral",
)

AGE_BUCKETS = ("18-24", "25-34", "35-44", "45-54", "55-64", "65+")

# US state -> census region (simplified)
US_STATE_TO_REGION: dict[str, str] = {
    "CT": "Northeast",
    "ME": "Northeast",
    "MA": "Northeast",
    "NH": "Northeast",
    "RI": "Northeast",
    "VT": "Northeast",
    "NJ": "Northeast",
    "NY": "Northeast",
    "PA": "Northeast",
    "IL": "Midwest",
    "IN": "Midwest",
    "MI": "Midwest",
    "OH": "Midwest",
    "WI": "Midwest",
    "IA": "Midwest",
    "KS": "Midwest",
    "MN": "Midwest",
    "MO": "Midwest",
    "NE": "Midwest",
    "ND": "Midwest",
    "SD": "Midwest",
    "DE": "South",
    "FL": "South",
    "GA": "South",
    "MD": "South",
    "NC": "South",
    "SC": "South",
    "VA": "South",
    "DC": "South",
    "WV": "South",
    "AL": "South",
    "KY": "South",
    "MS": "South",
    "TN": "South",
    "AR": "South",
    "LA": "South",
    "OK": "South",
    "TX": "South",
    "AZ": "West",
    "CO": "West",
    "ID": "West",
    "MT": "West",
    "NV": "West",
    "NM": "West",
    "UT": "West",
    "WY": "West",
    "AK": "West",
    "CA": "West",
    "HI": "West",
    "OR": "West",
    "WA": "West",
}

SEVERITY_ORDER = {"mild": 0, "moderate": 1, "severe": 2}
DURATION_ORDER = {"<6mo": 0, "6-12mo": 1, "1-3yr": 2, "3+yr": 3}
