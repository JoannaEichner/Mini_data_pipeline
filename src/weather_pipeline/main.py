import requests

from src.weather_pipeline.extract import extract_weather_data
from src.weather_pipeline.transform import transform_weather_data
from src.weather_pipeline.load import save_weather_data, save_weather_data_to_csv
from src.weather_pipeline.config import load_cities


def main() -> None:
    cities = load_cities("config/cities.json")
    weather_results = []
    for city in cities:
        try:
            raw_data = extract_weather_data(city)
        except requests.RequestException as error:
            print(f"Failed to fetch weather data for {city['name']}: {error}")
            continue

        tranformed_data = transform_weather_data(city, raw_data)
        weather_results.append(tranformed_data)

        save_weather_data(weather_results, "data/weather_data.json")
        save_weather_data_to_csv(weather_results, "data/weather_data.csv")

        print("Weather data saved to data/weather_data.json")
        print("Weather data saved to data/weather_data.csv")

if __name__ == "__main__":
    main()

    