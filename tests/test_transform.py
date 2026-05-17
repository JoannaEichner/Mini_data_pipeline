from src.weather_pipeline.transform import transform_weather_data
import pytest

def test_transform_weather_data_returns_clean_weather_record():
    city = {
        "name": "Warsaw",
        "latitude": 52.2297,
        "longitude": 21.0122,
    }

    raw_data = {
        "current_weather": {
            "temperature": 20.5,
            "windspeed": 7.2,
            "time": "2026-05-17T12:00",
        }
    }

    result = transform_weather_data(city, raw_data)

    assert result["city"] == "Warsaw"
    assert result["temperature"] == 20.5
    assert result["windspeed"] == 7.2
    assert result["time"] == "2026-05-17T12:00"

def test_transform_weather_data_raises_error_when_current_weather_missing():
    city = {
        "name": "Warsaw",
        "latitude": 52.2297,
        "longitude": 21.0122,
    }

    raw_data = {}

    with pytest.raises(KeyError):
        transform_weather_data(city, raw_data)