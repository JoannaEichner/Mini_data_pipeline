from unittest.mock import MagicMock, patch

from src.weather_pipeline.database import create_weather_table, insert_weather_data, save_weather_data_to_database

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

def test_save_weather_data_to_database_creates_table_and_inserts_data():
    data = [
        {
           "city": "Warsaw",
            "temperature": 20.5,
            "windspeed": 7.2,
            "time": "2026-05-17T12:00",
        }
    ]

    fake_conn = MagicMock()

    with (
        patch("src.weather_pipeline.database.get_db_connection") as mock_get_connection,
        patch("src.weather_pipeline.database.create_weather_table") as mock_create_table,
        patch("src.weather_pipeline.database.insert_weather_data") as mock_insert_data,
    ):
        mock_get_connection.return_value.__enter__.return_value = fake_conn

        save_weather_data_to_database(data)

    mock_create_table.assert_called_once_with(fake_conn)
    mock_insert_data.assert_called_once_with(fake_conn, data)