from __future__ import annotations

import pandas as pd


def find_host(dataframe: pd.DataFrame, host_id: str) -> pd.DataFrame:
    if host_id is None:
        return dataframe.iloc[0:0].copy()

    normalized_id = str(host_id).strip()
    if not normalized_id:
        return dataframe.iloc[0:0].copy()

    return dataframe[dataframe["host_id"].astype(str).str.strip() == normalized_id].copy()


def find_by_location(dataframe: pd.DataFrame, location: str) -> pd.DataFrame:
    if location is None:
        return dataframe.iloc[0:0].copy()

    normalized = str(location).strip()
    if not normalized:
        return dataframe.iloc[0:0].copy()

    return dataframe[
        dataframe["host_location"].fillna("").astype(str).str.lower() == normalized.lower()
    ].copy()


def find_by_room_type(dataframe: pd.DataFrame, room_type: str) -> pd.DataFrame:
    if room_type is None:
        return dataframe.iloc[0:0].copy()

    normalized = str(room_type).strip()
    if not normalized:
        return dataframe.iloc[0:0].copy()

    return dataframe[
        dataframe["room_type"].fillna("").astype(str).str.lower().str.contains(normalized.lower())
    ].copy()


def review_summary_by_location(dataframe: pd.DataFrame, location: str) -> pd.DataFrame:
    matches = find_by_location(dataframe, location)
    if matches.empty:
        return matches

    return matches[
        [
            "host_id",
            "host_name",
            "host_location",
            "room_type",
            "review_scores_rating",
            "review_scores_accuracy",
            "review_scores_cleanliness",
        ]
    ].copy()
