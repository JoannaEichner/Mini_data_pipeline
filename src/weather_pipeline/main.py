import requests

from src.weather_pipeline.extract import extract_weather_data
from src.weather_pipeline.transform import transform_weather_data
from src.weather_pipeline.load import save_weather_data

CITIES = [
    {"name": "Warsaw", "latitude": 52.2297, "longitude": 21.0122},
    {"name": "Krakow", "latitude": 50.0647, "longitude": 19.9450},
    {"name": "Gdansk", "latitude": 54.3520, "longitude": 18.6466},
]

def main() -> None:
    weather_results = []
    for city in CITIES:
        try:
            raw_data = extract_weather_data(city)
        except requests.RequestException as error:
            print(f"Failed to fetch weather data for {city['name']}: {error}")
            continue

        tranformed_data = transform_weather_data(city, raw_data)
        weather_results.append(tranformed_data)

        save_weather_data(weather_results, "data/weather_data.json")
        print("Weather data saved to data/weather_data.json")

if __name__ == "__main__":
    main()

    