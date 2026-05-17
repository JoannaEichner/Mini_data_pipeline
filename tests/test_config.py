import json

from src.weather_pipeline.config import load_cities


def test_load_cities_returns_list_of_cities(tmp_path):
    cities = [
        {
            "name": "Warsaw",
            "latitude": 52.2297,
            "longitude": 21.0122,
        }
    ]

    config_path = tmp_path / "cities.json"
    config_path.write_text(json.dumps(cities), encoding="utf-8")

    result = load_cities(config_path)

    assert result == cities