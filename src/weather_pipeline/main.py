import requests

from src.weather_pipeline.config import load_cities
from src.weather_pipeline.extract import extract_weather_data
from src.weather_pipeline.load import save_weather_data, save_weather_data_to_csv
from src.weather_pipeline.transform import transform_weather_data
from src.weather_pipeline.database import (
    create_weather_table,
    get_db_connection,
    insert_weather_data,
)


def main() -> None:
    cities = load_cities("config/cities.json")
    weather_results = []
    for city in cities:
        try:
            raw_data = extract_weather_data(city)
        except requests.RequestException as error:
            print(f"Failed to fetch weather data for {city['name']}: {error}")
            continue

        transformed_data = transform_weather_data(city, raw_data)
        weather_results.append(transformed_data)

    save_weather_data(weather_results, "data/weather_data.json")
    save_weather_data_to_csv(weather_results, "data/weather_data.csv")

    print("Weather data saved to data/weather_data.json")
    print("Weather data saved to data/weather_data.csv")

    with get_db_connection() as conn:
        create_weather_table(conn)
        insert_weather_data(conn, weather_results)

        print("Weather data saved to PostgreSQL")




if __name__ == "__main__":
    main()

    