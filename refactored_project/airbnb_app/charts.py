from __future__ import annotations

from pathlib import Path

import matplotlib

import matplotlib.pyplot as plt
import pandas as pd


def _ensure_directory(output_dir: str | Path) -> Path:
    directory = Path(output_dir)
    directory.mkdir(parents=True, exist_ok=True)
    return directory


def _show_or_close(fig, show: bool) -> None:
    if show:
        plt.show(block=False)
        plt.pause(0.1)
    else:
        plt.close(fig)


def save_bedroom_distribution(
    dataframe: pd.DataFrame, output_dir: str | Path = "charts", show: bool = False
) -> str:
    directory = _ensure_directory(output_dir)
    counts = dataframe["bedrooms"].dropna().astype(int).value_counts().sort_index()

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.pie(counts.values, labels=[str(value) for value in counts.index], autopct="%1.1f%%")
    ax.set_title("Bedroom Distribution")
    path = directory / "bedroom_distribution.png"
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    _show_or_close(fig, show)
    return str(path)


def save_room_type_distribution(
    dataframe: pd.DataFrame, output_dir: str | Path = "charts", show: bool = False
) -> str:
    directory = _ensure_directory(output_dir)
    counts = dataframe["room_type"].fillna("").astype(str).value_counts().sort_values(ascending=False)

    fig, ax = plt.subplots(figsize=(9, 6))
    bars = ax.bar(counts.index.astype(str), counts.values, color="steelblue")
    ax.set_title("Room Type Distribution")
    ax.set_xlabel("Room Type")
    ax.set_ylabel("Count")
    ax.bar_label(bars, padding=3)
    plt.xticks(rotation=20)
    path = directory / "room_type_distribution.png"
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    _show_or_close(fig, show)
    return str(path)


def save_accommodates_vs_price(
    dataframe: pd.DataFrame, output_dir: str | Path = "charts", show: bool = False
) -> str:
    directory = _ensure_directory(output_dir)
    grouped = dataframe.groupby("accommodates")["price"].mean().dropna()

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(grouped.index, grouped.values, color="darkgreen")
    ax.set_title("Average Price by Accommodation Count")
    ax.set_xlabel("Accommodates")
    ax.set_ylabel("Average Price")
    path = directory / "accommodates_vs_price.png"
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    _show_or_close(fig, show)
    return str(path)


def save_price_trends(
    dataframe: pd.DataFrame, output_dir: str | Path = "charts", show: bool = False
) -> str:
    directory = _ensure_directory(output_dir)
    trend_frame = dataframe.copy()
    trend_frame["host_since"] = pd.to_datetime(
        trend_frame["host_since"], format="%d-%m-%y", errors="coerce"
    )
    trend_frame = trend_frame.dropna(subset=["host_since", "price"])

    yearly = trend_frame.groupby(trend_frame["host_since"].dt.year)["price"].mean()

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(yearly.index.astype(str), yearly.values, marker="o", color="royalblue")
    ax.set_title("Average Price by Year")
    ax.set_xlabel("Year")
    ax.set_ylabel("Average Price")
    fig.autofmt_xdate()
    path = directory / "price_trends.png"
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    _show_or_close(fig, show)
    return str(path)


def save_all_charts(dataframe: pd.DataFrame, output_dir: str | Path = "charts") -> dict[str, str]:
    return {
        "bedroom_distribution": save_bedroom_distribution(dataframe, output_dir),
        "room_type_distribution": save_room_type_distribution(dataframe, output_dir),
        "accommodates_vs_price": save_accommodates_vs_price(dataframe, output_dir),
        "price_trends": save_price_trends(dataframe, output_dir),
    }
