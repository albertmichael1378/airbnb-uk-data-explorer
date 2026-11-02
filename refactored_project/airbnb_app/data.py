from __future__ import annotations

from pathlib import Path
from typing import Union

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DATASET = PROJECT_ROOT.parent / "Airbnb_UK_2022.csv"
REQUIRED_COLUMNS = [
    "host_id",
    "name",
    "host_name",
    "host_since",
    "host_location",
    "property_type",
    "room_type",
    "accommodates",
    "bathrooms_text",
    "bedrooms",
    "beds",
    "price",
    "review_scores_rating",
    "review_scores_accuracy",
    "review_scores_cleanliness",
]


def _clean_price(series: pd.Series) -> pd.Series:
    cleaned = series.astype(str).str.replace("£", "", regex=False)
    cleaned = cleaned.str.replace(",", "", regex=False)
    cleaned = cleaned.str.replace("$", "", regex=False)
    cleaned = cleaned.str.replace("[^0-9.-]", "", regex=True)
    return pd.to_numeric(cleaned, errors="coerce")


def load_dataset(path: Union[str, Path, None] = None) -> pd.DataFrame:
    """Load and normalize the Airbnb dataset."""
    dataset_path = Path(path) if path is not None else DEFAULT_DATASET

    if not dataset_path.exists():
        raise FileNotFoundError(f"Dataset not found: {dataset_path}")

    dataframe = pd.read_csv(dataset_path, encoding="latin-1")
    missing = [column for column in REQUIRED_COLUMNS if column not in dataframe.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    cleaned = dataframe.copy()
    cleaned["host_id"] = cleaned["host_id"].astype(str).str.strip()
    cleaned["host_name"] = cleaned["host_name"].fillna("").astype(str).str.strip()
    cleaned["host_location"] = cleaned["host_location"].fillna("").astype(str).str.strip()
    cleaned["room_type"] = cleaned["room_type"].fillna("").astype(str).str.strip()
    cleaned["property_type"] = cleaned["property_type"].fillna("").astype(str).str.strip()
    cleaned["price"] = _clean_price(cleaned["price"])
    cleaned["accommodates"] = pd.to_numeric(cleaned["accommodates"], errors="coerce")
    cleaned["bedrooms"] = pd.to_numeric(cleaned["bedrooms"], errors="coerce")
    cleaned["beds"] = pd.to_numeric(cleaned["beds"], errors="coerce")
    cleaned["review_scores_rating"] = pd.to_numeric(
        cleaned["review_scores_rating"], errors="coerce"
    )
    cleaned["review_scores_accuracy"] = pd.to_numeric(
        cleaned["review_scores_accuracy"], errors="coerce"
    )
    cleaned["review_scores_cleanliness"] = pd.to_numeric(
        cleaned["review_scores_cleanliness"], errors="coerce"
    )

    return cleaned
