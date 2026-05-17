def transform_weather_data(city: dict, raw_data: dict) -> dict:
    current_weather = raw_data["current_weather"]

    return {
        "city": city["name"],
        "temperature": current_weather["temperature"],
        "windspeed": current_weather["windspeed"],
        "time": current_weather["time"],
    }

