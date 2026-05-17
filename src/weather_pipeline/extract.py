import requests #biblioteka do robienia requestów do zewnętrznych API

def extract_weather_data(city: dict) -> dict:
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": city["latitude"],
        "longitude": city["longitude"],
        "current_weather": True,
    }

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()

    return response.json()
