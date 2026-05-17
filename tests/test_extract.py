from unittest.mock import Mock, patch

from src.weather_pipeline.extract import extract_weather_data

def test_extract_weather_data_returns_json_response():
    city = {
        "name": "Warsaw",
        "latitude": 52.2297,
        "longitude": 21.0122,
    }

    expected_data = {
        "current_weather": {
            "temperature": 20.5,
            "windspeed": 7.2,
            "time": "2026-05-17T12:00",
        }
    }


    fake_response = Mock()
    fake_response.json.return_value = expected_data

    with patch("src.weather_pipeline.extract.requests.get") as mock_get:
        mock_get.return_value = fake_response

        result = extract_weather_data(city)

    mock_get.assert_called_once_with(
        "https://api.open-meteo.com/v1/forecast",
        params={
            "latitude": 52.2297,
            "longitude": 21.0122,
            "current_weather": True,
        },
        timeout=10,
    )

    assert result == expected_data