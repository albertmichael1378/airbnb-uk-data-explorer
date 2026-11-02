# Project Details and Workflow

## Purpose

This project was created to analyze Airbnb UK listing data and answer practical questions through direct search and visual summaries. It combines CSV file handling, Python logic, and plotting functions in a simple beginner-friendly workflow.

## What the project does

The application can:

- open a CSV dataset
- iterate through rows and filter records
- search by host ID
- search by host location
- query property information by room type and listing attributes
- inspect review score metrics
- generate visual charts for understanding data patterns

## Main script behavior

### Search mode
The interactive search flow is managed in `query_app.py`.

The app repeatedly asks for inputs such as:

- host ID
- host location
- property type
- location for review details

It validates the input and calls helper functions from `components.py` to fetch and print matching records.

### Visualization mode
The notebook `system1.ipynb` acts as the main orchestrator. It gives the user menu choices for:

- bedroom proportion chart
- bar chart of room types
- scatter plot of accommodation and price
- price trend line graphs for 2019–2022

The plotting logic is implemented in `matplo.py`.

## Core functions

### `opening_file()`
Used to ask the user for a file path and open the CSV file safely.

### `hostid_search(host_id, csv_file)`
Searches the CSV dataset for a matching host ID and prints the host details related to that row.

### `location_search(host_location, csv_file)`
Searches the dataset for listings from a selected location and prints matching records.

### `ptp_search(csv_file, ptp_type)`
Looks for property values based on room type and related attributes.

### `review_search(csv_file, R)`
Prints review score values associated with a location.

## Data analysis emphasis

The project focuses on the following analytical themes:

- Frequency of property types
- Average price trends by accommodation size
- Distribution of bedrooms across listings
- Relationship between accommodate count and listing price
- Historic pricing trends over several years

## Suggested workflow for a new user

1. Activate the environment.
2. Install dependencies from `requirements.txt`.
3. Open the notebook `system1.ipynb`.
4. Select the search or chart option.
5. Enter the required values in the prompts.
6. Analyze the printed records and generated charts.

## Recommended environment

- Python 3.x
- Jupyter Notebook or VS Code notebook support
- pandas
- matplotlib

## Learning value

This project is a useful example of:

- reading CSV datasets in Python
- building simple data queries
- filtering rows based on conditions
- generating meaningful business insights from a dataset
- creating descriptive charts from real data

## Final note

The project is small, practical, and designed for learning and exploration rather than deployment. It demonstrates how a dataset can be turned into a simple interactive data analysis app using Python.
