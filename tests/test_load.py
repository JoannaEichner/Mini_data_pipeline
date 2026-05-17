import json

from src.weather_pipeline.load import save_weather_data

def test_save_weather_data_creates_json_file(tmp_path):
    data = [
        {
            "city": "Warsaw",
            "temperature": 20.5,
            "windspeed": 7.2,
            "time": "2026-05-17T12:00",
        }
    ]

    output_path = tmp_path / "weather_data.json"

    save_weather_data(data, output_path)

    assert output_path.exists()

    saved_data = json.loads(output_path.read_text(encoding="utf-8"))

    assert saved_data == data