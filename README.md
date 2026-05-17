# Mini Data Pipeline

A simple Python ETL pipeline that fetches current weather data from the Open-Meteo API, transforms the response, and saves the output to JSON and CSV files.

## Project goal

The goal of this project is to practice building a small data pipeline in Python using a clean project structure, modular code, tests, and basic code quality tools.

The pipeline follows a simple ETL process:

```text
Extract → Transform → Load
```

## Features

- Fetches current weather data from a public API
- Reads city configuration from `config/cities.json`
- Transforms raw API responses into a clean data format
- Saves results to JSON
- Saves results to CSV
- Includes unit tests
- Uses Ruff for code quality checks
- Handles API request errors without stopping the whole pipeline

## Project structure

```text
Mini_data_pipeline/
├── config/
│   └── cities.json
├── data/
│   ├── weather_data.json
│   └── weather_data.csv
├── src/
│   ├── __init__.py
│   └── weather_pipeline/
│       ├── __init__.py
│       ├── config.py
│       ├── extract.py
│       ├── transform.py
│       ├── load.py
│       └── main.py
├── tests/
│   ├── test_config.py
│   ├── test_extract.py
│   ├── test_load.py
│   └── test_transform.py
├── .gitignore
├── README.md
└── requirements.txt
```

## How it works

### 1. Extract

The pipeline fetches weather data from the Open-Meteo API for cities defined in:

```text
config/cities.json
```

Example city configuration:

```json
{
    "name": "Warsaw",
    "latitude": 52.2297,
    "longitude": 21.0122
}
```

### 2. Transform

The raw API response is transformed into a clean structure:

```json
{
    "city": "Warsaw",
    "temperature": 20.5,
    "windspeed": 7.2,
    "time": "2026-05-17T12:00"
}
```

### 3. Load

The transformed data is saved to:

```text
data/weather_data.json
data/weather_data.csv
```

## Requirements

- Python 3.13+
- requests
- pytest
- ruff

## Installation

Create and activate a virtual environment:

```powershell
python -m venv .venv
.venv\Scripts\activate
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

## How to run the pipeline

From the main project directory, run:

```powershell
python -m src.weather_pipeline.main
```

After running the pipeline, output files will be created in the `data/` directory.

## How to run tests

```powershell
python -m pytest
```

Expected result:

```text
tests/test_config.py .
tests/test_extract.py .
tests/test_load.py ..
tests/test_transform.py ..
```

## How to run Ruff

```powershell
python -m ruff check .
```

Expected result:

```text
All checks passed!
```

## Example output

JSON output example:

```json
[
    {
        "city": "Warsaw",
        "temperature": 20.5,
        "windspeed": 7.2,
        "time": "2026-05-17T12:00"
    }
]
```

CSV output example:

```csv
city,temperature,windspeed,time
Warsaw,20.5,7.2,2026-05-17T12:00
```

## Tests

The project includes tests for:

- loading city configuration from JSON
- extracting data from the API using a mocked request
- transforming raw weather data
- saving data to JSON
- saving data to CSV

The API test uses mocking, so tests do not depend on an internet connection.

## Notes

Generated output files in the `data/` directory should not be committed to the repository.

Recommended `.gitignore` entries:

```gitignore
.venv/
__pycache__/
*.pyc
data/*.json
data/*.csv
.env
```

## Next steps

Planned improvements:

- save weather data to PostgreSQL
- add Docker support
- add pipeline orchestration with Prefect or Airflow
- add logging
- add environment-based configuration