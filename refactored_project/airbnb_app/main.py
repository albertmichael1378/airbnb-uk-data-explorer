from __future__ import annotations

import argparse
from pathlib import Path

from .charts import (
    save_accommodates_vs_price,
    save_all_charts,
    save_bedroom_distribution,
    save_price_trends,
    save_room_type_distribution,
)
from .data import load_dataset
from .search import find_by_location, find_by_room_type, find_host, review_summary_by_location


def print_host_results(dataframe):
    if dataframe.empty:
        print("No host matches found.")
        return

    print(dataframe[["host_id", "host_name", "host_location", "room_type", "price"]].head(10).to_string(index=False))


def print_location_results(dataframe):
    if dataframe.empty:
        print("No listings found for that location.")
        return

    print(dataframe[["host_id", "host_name", "host_location", "room_type", "price"]].head(10).to_string(index=False))


def print_room_results(dataframe):
    if dataframe.empty:
        print("No listings found for that room type.")
        return

    print(dataframe[["host_id", "host_name", "room_type", "property_type", "price"]].head(10).to_string(index=False))


def print_review_results(dataframe):
    if dataframe.empty:
        print("No review data found for that location.")
        return

    print(dataframe.to_string(index=False))


def generate_charts_menu(dataframe, output_dir: Path = Path("charts")) -> None:
    chart_options = {
        "1": ("Bedroom distribution", save_bedroom_distribution),
        "2": ("Room type distribution", save_room_type_distribution),
        "3": ("Average price by accommodation count", save_accommodates_vs_price),
        "4": ("Average price by host registration year", save_price_trends),
    }

    while True:
        print("\nAvailable charts")
        for choice, (name, _) in chart_options.items():
            print(f"{choice}. {name}")
        print("5. Generate all charts")
        print("0. Back to main menu")

        choice = input("Choose a chart: ").strip().lower()

        if choice in {"0", "b", "back"}:
            return
        if choice == "5":
            saved = save_all_charts(dataframe, output_dir)
        elif choice in chart_options:
            name, save_chart = chart_options[choice]
            saved = {name: save_chart(dataframe, output_dir, show=True)}
        else:
            print("Invalid option, please choose an available chart.")
            continue

        print("Chart saved to:" if len(saved) == 1 else "Charts saved to:")
        for name, path in saved.items():
            print(f"- {name}: {path}")


def run_interactive(dataset_path: str | None = None) -> None:
    dataframe = load_dataset(dataset_path)

    while True:
        print("\nAirbnb UK Dashboard")
        print("1. Search by host ID")
        print("2. Search by location")
        print("3. Search by room type")
        print("4. Review scores by location")
        print("5. Generate charts")
        print("q. Quit")

        choice = input("Choose an option: ").strip().lower()

        if choice in {"q", "quit", "exit"}:
            print("Goodbye!")
            break

        if choice == "1":
            host_id = input("Enter host ID: ").strip()
            results = find_host(dataframe, host_id)
            print_host_results(results)
        elif choice == "2":
            location = input("Enter location: ").strip()
            results = find_by_location(dataframe, location)
            print_location_results(results)
        elif choice == "3":
            room_type = input("Enter room type (example: home/apt): ").strip()
            results = find_by_room_type(dataframe, room_type)
            print_room_results(results)
        elif choice == "4":
            location = input("Enter location: ").strip()
            results = review_summary_by_location(dataframe, location)
            print_review_results(results)
        elif choice == "5":
            generate_charts_menu(dataframe)
        else:
            print("Invalid option, please try again.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Airbnb UK Data Explorer")
    parser.add_argument("--dataset", type=str, help="Path to the Airbnb CSV file")
    args = parser.parse_args()

    if args.dataset:
        dataframe = load_dataset(args.dataset)
        print("Dataset loaded successfully.")
        print(f"Rows: {len(dataframe)}")
        print("Use the interactive menu by running without --dataset.")
        return

    run_interactive()


if __name__ == "__main__":
    main()
