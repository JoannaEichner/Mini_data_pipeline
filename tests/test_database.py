from unittest.mock import MagicMock

from src.weather_pipeline.database import create_weather_table, insert_weather_data

def test_create_weather_table_executes_query_and_commits():
    conn = MagicMock()
    cursor = MagicMock()

    conn.cursor.return_value.__enter__.return_value = cursor

    create_weather_table(conn)

    cursor.execute.assert_called_once()
    conn.commit.assert_called_once()


def test_insert_weather_data_inserts_records_and_commits():
    conn = MagicMock()
    cursor = MagicMock()

    conn.cursor.return_value.__enter__.return_value = cursor

    data = [
        {
            "city": "Warsaw",
            "temperature": 20.5,
            "windspeed": 7.2,
            "time": "2026-05-17T12:00",
        },
        {
            "city": "Krakow",
            "temperature": 21.0,
            "windspeed": 5.5,
            "time": "2026-05-17T12:00",
        }
    ]

    insert_weather_data(conn, data)

    assert cursor.execute.call_count == 2
    conn.commit.assert_called_once()