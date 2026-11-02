from __future__ import annotations

import sys
import tempfile
import unittest
import warnings
from pathlib import Path
from unittest.mock import patch

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from airbnb_app.charts import save_all_charts, save_bedroom_distribution, save_price_trends
from airbnb_app.data import DEFAULT_DATASET, load_dataset
from airbnb_app.main import generate_charts_menu
from airbnb_app.search import find_by_location, find_by_room_type, find_host


class AirbnbAppTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dataframe = load_dataset(DEFAULT_DATASET)

    def test_dataset_loads(self):
        self.assertGreater(len(self.dataframe), 0)
        self.assertIn("host_id", self.dataframe.columns)
        self.assertIn("room_type", self.dataframe.columns)

    def test_host_search_returns_matches(self):
        host_id = str(self.dataframe["host_id"].iloc[0])
        matches = find_host(self.dataframe, host_id)
        self.assertGreater(len(matches), 0)

    def test_location_search_returns_matches(self):
        location = str(self.dataframe["host_location"].iloc[0])
        matches = find_by_location(self.dataframe, location)
        self.assertGreater(len(matches), 0)

    def test_room_type_search_returns_matches(self):
        room_type = str(self.dataframe["room_type"].dropna().iloc[0])
        matches = find_by_room_type(self.dataframe, room_type)
        self.assertGreater(len(matches), 0)

    def test_charts_are_created(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            saved = save_all_charts(self.dataframe, temp_dir)
            self.assertTrue(all(Path(path).exists() for path in saved.values()))

    def test_price_trend_parses_dates_without_format_warning(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            with warnings.catch_warnings(record=True) as caught:
                warnings.simplefilter("always")
                path = save_price_trends(self.dataframe, temp_dir)
                self.assertTrue(Path(path).exists())

        self.assertFalse(any("Could not infer format" in str(item.message) for item in caught))

    def test_selected_chart_opens_without_blocking_menu(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            with (
                patch("matplotlib.pyplot.show") as show,
                patch("matplotlib.pyplot.pause") as pause,
            ):
                path = save_bedroom_distribution(self.dataframe, temp_dir, show=True)
                show.assert_called_once_with(block=False)
                pause.assert_called_once_with(0.1)
                self.assertTrue(Path(path).exists())
                self.assertTrue(plt.get_fignums())

        plt.close("all")

    def test_chart_menu_generates_selected_chart(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            output_dir = Path(temp_dir)
            with (
                patch("builtins.input", side_effect=["1", "2", "0"]),
                patch(
                    "airbnb_app.main.save_bedroom_distribution",
                    return_value=str(output_dir / "bedroom_distribution.png"),
                ) as save_chart,
                patch(
                    "airbnb_app.main.save_room_type_distribution",
                    return_value=str(output_dir / "room_type_distribution.png"),
                ) as save_second_chart,
                patch("airbnb_app.main.save_all_charts") as save_all,
            ):
                generate_charts_menu(self.dataframe, output_dir)

        save_chart.assert_called_once_with(self.dataframe, output_dir, show=True)
        save_second_chart.assert_called_once_with(self.dataframe, output_dir, show=True)
        save_all.assert_not_called()


if __name__ == "__main__":
    unittest.main()
