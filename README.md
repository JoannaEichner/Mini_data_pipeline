# Mini Data Pipeline

A simple Python ETL pipeline that fetches current weather data from the Open-Meteo API, transforms the response, and saves the output to JSON, CSV, and PostgreSQL.

## Project goal

The goal of this project is to practice building a small data pipeline in Python using a clean project structure, modular code, tests, PostgreSQL, Docker Compose, and basic code quality tools.

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
- Saves results to PostgreSQL
- Runs PostgreSQL in a Docker container using Docker Compose
- Creates the PostgreSQL table automatically if it does not exist
- Prevents duplicate records using a unique constraint on city and measurement time
- Includes unit tests
- Uses mocking for API and database-related tests
- Uses Ruff for code quality checks
- Handles API request errors without stopping the whole pipeline

## Project structure

```text
Mini_data_pipeline/
├── config/
│   └── cities.json
├── data/
│   └── generated output files
├── src/
│   ├── __init__.py
│   └── weather_pipeline/
│       ├── __init__.py
│       ├── config.py
│       ├── database.py
│       ├── extract.py
│       ├── transform.py
│       ├── load.py
│       └── main.py
├── tests/
│   ├── test_config.py
│   ├── test_database.py
│   ├── test_extract.py
│   ├── test_load.py
│   └── test_transform.py
├── .env.example
├── .gitignore
├── docker-compose.yml
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
PostgreSQL table: weather_measurements
```

## PostgreSQL output

The pipeline saves transformed weather data to a PostgreSQL database.

### Database table

The pipeline creates a table named:

```sql
weather_measurements
```

Table schema:

```sql
CREATE TABLE IF NOT EXISTS weather_measurements (
    id SERIAL PRIMARY KEY,
    city TEXT NOT NULL,
    temperature DOUBLE PRECISION NOT NULL,
    windspeed DOUBLE PRECISION NOT NULL,
    measurement_time TIMESTAMP NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (city, measurement_time)
);
```

The unique constraint prevents inserting duplicate records for the same city and measurement time.

## Docker Compose

The project includes a `docker-compose.yml` file that runs PostgreSQL in a Docker container.

### Start PostgreSQL with Docker

```powershell
docker compose up -d
```

This starts a PostgreSQL container named:

```text
weather_pipeline_postgres
```

The database is available on:

```text
localhost:5433
```

Inside the container, PostgreSQL runs on port `5432`, but it is exposed to the host machine as `5433`.

### Check running containers

```powershell
docker ps
```

### Connect to PostgreSQL inside the container

```powershell
docker exec -it weather_pipeline_postgres psql -U postgres -d weather_pipeline_db
```

Inside `psql`, you can check existing tables:

```sql
SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'public';
```

You can check saved weather data with:

```sql
SELECT *
FROM weather_measurements;
```

To exit `psql`:

```sql
\q
```

### Stop the container

```powershell
docker compose down
```

## Environment variables

Create a `.env` file in the main project directory.

When using Docker Compose, use:

```env
DB_HOST=localhost
DB_PORT=5433
DB_NAME=weather_pipeline_db
DB_USER=postgres
DB_PASSWORD=postgres
```

The `.env` file is ignored by Git and should not be committed.

The repository includes `.env.example` as a safe example configuration file.

## Requirements

- Python 3.13+
- Docker Desktop
- requests
- pytest
- ruff
- psycopg2-binary
- python-dotenv

## Installation

Create and activate a virtual environment:

```powershell
python -m venv .venv
.venv\Scripts\activate
```

Install Python dependencies:

```powershell
pip install -r requirements.txt
```

## How to run the pipeline

Start PostgreSQL first:

```powershell
docker compose up -d
```

Then run the pipeline from the main project directory:

```powershell
python -m src.weather_pipeline.main
```

After running the pipeline, output data will be saved to:

- `data/weather_data.json`
- `data/weather_data.csv`
- PostgreSQL table `weather_measurements`

## How to run tests

```powershell
python -m pytest
```

Expected result:

```text
tests/test_config.py .
tests/test_database.py ...
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

PostgreSQL output example:

```text
id | city   | temperature | windspeed | measurement_time     | created_at
1  | Warsaw | 20.5        | 7.2       | 2026-05-17 12:00:00  | 2026-05-17 12:01:00
```

## Tests

The project includes tests for:

- loading city configuration from JSON
- extracting data from the API using a mocked request
- transforming raw weather data
- saving data to JSON
- saving data to CSV
- creating the PostgreSQL table
- inserting weather records into PostgreSQL
- saving data to the database using mocked database functions

The API and database tests use mocking, so unit tests do not depend on an internet connection or a live database.

## Notes

Generated output files in the `data/` directory should not be committed to the repository.

The `.env` file contains local database credentials and should not be committed.

Recommended `.gitignore` entries:

```gitignore
.venv/
__pycache__/
*.pyc
data/*.json
data/*.csv
.env
```

## Useful commands

Start PostgreSQL:

```powershell
docker compose up -d
```

Stop PostgreSQL:

```powershell
docker compose down
```

Run pipeline:

```powershell
python -m src.weather_pipeline.main
```

Run tests:

```powershell
python -m pytest
```

Run Ruff:

```powershell
python -m ruff check .
```

Connect to PostgreSQL container:

```powershell
docker exec -it weather_pipeline_postgres psql -U postgres -d weather_pipeline_db
```

## Next steps

Planned improvements:

- add pipeline orchestration with Prefect or Airflow
- add logging
- add environment-based configuration
- add database migrations
- add integration tests for PostgreSQL