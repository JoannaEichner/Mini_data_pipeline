import os
from typing import Any

import psycopg2
from dotenv import load_dotenv
from psycopg2.extensions import connection

load_dotenv()

def get_db_connection() -> connection:
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
    )

def create_weather_table(conn: connection) -> None:
    query = """
        CREATE TABLE IF NOT EXISTS weather_measurements (
            id SERIAL PRIMARY KEY,
            city TEXT NOT NULL,
            temperature DOUBLE PRECISION NOT NULL,
            windspeed DOUBLE PRECISION NOT NULL,
            measurement_time TIMESTAMP NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """

    with conn.cursor() as cursor:
        cursor.execute(query)

    conn.commit()

def insert_weather_data(conn: connection, data: list[dict[str, Any]]) -> None:
    query = """
        INSERT INTO weather_measurements (
            city,
            temperature,
            windspeed,
            measurement_time
        )
        VALUES (%s, %s, %s, %s);
    """

    with conn.cursor() as cursor:
        for record in data:
            cursor.execute(
                query,
                (
                    record["city"],
                    record["temperature"],
                    record["windspeed"],
                    record["time"],
                ),
            )