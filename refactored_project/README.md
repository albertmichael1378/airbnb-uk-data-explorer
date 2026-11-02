# Refactored Airbnb UK Data Explorer

This folder contains a cleaner, more maintainable version of the original Airbnb analysis project.

## Overview

The app reads the Airbnb UK dataset, lets the user search records, and generates charts for key analysis questions.

## Goals of this refactor

- fix the original logic issues
- keep the code easier to read and maintain
- organize the project into a cleaner structure
- separate data, search, and chart logic
- preserve the original project while creating a safer working version in a subfolder

## Project structure

```text
refactored_project/
├── airbnb_app/
│   ├── __init__.py
│   ├── charts.py
│   ├── data.py
│   ├── main.py
│   └── search.py
├── tests/
│   └── test_app.py
├── README.md
├── requirements.txt
└── run.py
```

## How to run

```powershell
cd refactored_project
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python run.py
```

## Features

- search listings by host ID
- filter listings by location
- filter listings by room type
- view review summaries by area
- choose and generate a specific chart, or generate all charts, for bedroom distribution, room types, price trends, and accommodation-price relationship

Generated charts are saved as PNG files in the `charts/` directory. Selecting an individual chart opens it in a non-blocking Matplotlib window, so you can keep the chart open and select another. The chart menu stays open; choose **Generate all charts** (save-only) or **Back to main menu** when finished.

## Notes

This is still a lightweight analysis project, but it is structured much more cleanly than the original notebook-first version.
