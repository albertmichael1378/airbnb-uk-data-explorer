# Airbnb UK 2022 Data Explorer

A Python-based data analysis project for exploring Airbnb UK listing data using CSV queries and interactive visualizations.

## Contents

- [Project versions](#project-versions)
- [Legacy version features](#legacy-version-features)
- [Project Summary](#project-summary)
- [Why this project matters](#why-this-project-matters)
- [Key Features](#key-features)
- [Architecture Overview](#architecture-overview)
- [Project Structure](#project-structure)
- [Dataset Focus](#dataset-focus)
- [Screenshots](#screenshots)
- [Setup Instructions](#setup-instructions)
- [Running the Project](#running-the-project)
- [Example Usage Flow](#example-usage-flow)
- [Example Search Inputs](#example-search-inputs)
- [Notes and Limitations](#notes-and-limitations)
- [Technologies Used](#technologies-used)
- [Summary](#summary)

## Project versions

- **Current version:** See [`refactored_project/`](./refactored_project/README.md) for the actively maintained application.
- **Legacy version:** The original notebook and scripts are preserved for reference. They may contain bugs and are not the recommended way to run the project.

## Legacy version features

- Search listing data by host ID and host location.
- Filter listings using room and property attributes, and inspect review scores by location.
- Display charts for bedroom distribution, room-type counts, accommodation capacity versus price, and average prices grouped by host-registration dates.
- Use an interactive notebook menu and prompts to choose searches and charts.

The charts are displayed inline in the notebook, but they are static plots rather than interactive charts with controls such as zooming or filtering.

## Project Summary

This project was designed to help users analyze Airbnb listing data by:

- searching listings by host ID
- filtering by location and property type
- inspecting review-related metrics
- generating visual insights about pricing and listing distribution

The application combines Python scripting, pandas analysis, and matplotlib charts in a simple, beginner-friendly workflow for understanding a real-world dataset.

## Why this project matters

Airbnb listing datasets contain useful insights for:

- pricing analysis
- location-based comparisons
- market trend observation
- property type evaluation
- review quality assessment

This project demonstrates how those insights can be extracted from raw spreadsheet data using Python.

## Key Features

- Host lookup by ID
- Search by host location
- Property filtering by room type and listing attributes
- Review score analysis by region
- Visualization of pricing and accommodation trends
- Notebook-driven interactive data exploration

## Architecture Overview

```text
+-------------------+       +------------------+       +---------------------+
| User Input        | ----> | query_app.py     | ----> | components.py       |
| (host ID, location|       | search workflow  |       | CSV lookup logic    |
| room type, review)|       +------------------+       +---------------------+
+-------------------+                                           |
                                                                  v
                                                    +------------------+
                                                    | Airbnb CSV Data  |
                                                    | Airbnb_UK_2022.csv |
                                                    +------------------+
                                                                  |
                                                                  v
                                                    +------------------+
                                                    | matplo.py        |
                                                    | charts and plots |
                                                    +------------------+
                                                                  |
                                                                  v
                                                    +------------------+
                                                    | Notebook / User  |
                                                    | Output / Charts  |
                                                    +------------------+
```

## Project Structure

- `query_app.py` — interactive search workflow for the dataset
- `components.py` — helper functions for opening files and executing lookup logic
- `matplo.py` — visualization logic using pandas and matplotlib
- `system1.ipynb` — notebook-based entry point and user menu
- `Airbnb_UK_2022.csv` — main dataset used in the analysis
- `air.csv` — additional CSV file in the workspace
- `requirements.txt` — Python dependency list

## Dataset Focus

The dataset includes fields such as:

- host ID
- host name
- host location
- host since
- room type
- accommodates
- bathrooms text
- bedrooms
- beds
- price
- review score metrics

This makes it suitable for questions like:

- Which properties are available in a location?
- What types of listings are most common?
- How does accommodation count relate to price?
- What pricing patterns appear over time?

## Screenshots

> Add screenshots here to showcase the notebook flow, command-line UI, and generated charts.

### Example screenshot section

![App Menu](docs/images/app-menu.png)

![Search Output](docs/images/search-output.png)

![Charts](docs/images/charts.png)

If you want a cleaner GitHub presentation, place screenshots under a `docs/images/` folder and reference them here.

## Setup Instructions

### 1. Create and activate a virtual environment
On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2. Install dependencies
```powershell
pip install -r requirements.txt
```

## Running the Project

The main interactive flow is implemented in the notebook file: `system1.ipynb`.

Open the notebook in VS Code or Jupyter and run the cells. The app will ask for input such as:

- press `1` for data search mode
- press `2` for the bedroom pie chart
- press `3` for room type distribution bar chart
- press `4` for scatter plot of accommodation vs. price
- press `5` for line chart of Airbnb prices across 2019–2022
- press `7` for yearly price trend chart

The search workflow is also exposed through the Python functions in `query_app.py` and `components.py`.

## Example Usage Flow

1. Open the project notebook.
2. Enter `1` to go into the search mode.
3. Enter a host ID, location, or property type when prompted.
4. Use `back` to return to the visualization section when needed.
5. Choose chart options to display visuals.

## Example Search Inputs

- Host ID: a host number from the CSV
- Host location: London, Manchester, etc.
- Property type: values like shared room, private room, or entire home/apt
- Review location: a region or area found in the dataset

## Notes and Limitations

- This project is mainly a command-line and notebook-based analysis tool.
- It is not a polished web dashboard or production-ready API.
- The code is dataset-specific and depends on the structure of the Airbnb CSV file.
- Some functions are experimental or contain older debugging code remnants, but the overall workflow is usable for learning and exploratory analysis.

## Technologies Used

- Python
- Pandas
- Matplotlib
- CSV module
- Jupyter Notebook

## Summary

This project is a hands-on Airbnb data analysis application that demonstrates how to:

- load and inspect CSV data,
- query listing details,
- search records by important fields,
- produce meaningful visual summaries,
- and present a beginner-friendly analytics workflow in Python.

It is ideal for learning data exploration, file handling, search logic, and chart generation with real-world datasets.
