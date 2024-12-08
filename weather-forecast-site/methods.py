import json

from api_requests.main import (
    get_location,
    get_weather_by_location
)


def check_weather(weather_data):
    temperature = weather_data["temperature"][1]
    humidity = weather_data["humidity"][1]
    wind_speed = weather_data["wind_speed"][1]
    rain_prob = weather_data["rain_prob"][1]

    if temperature < -5 or temperature > 27:
        return False
    if humidity < 30 or humidity > 60:
        return False
    if humidity > 50 and (temperature < 5 or temperature > 25):
        return False
    if wind_speed > 36:  # шкала Бофорта
        return False
    if rain_prob > 60:
        return False
    return True


def get_weather(location, get_cached=False):
    if get_cached:
        with open("location.json", "r", encoding="utf-8") as file:
            location_data = json.load(file)
        localized_name = location_data[0]["LocalizedName"]

        with open("weather_data.json", "r", encoding="utf-8") as file:
            data = json.load(file)
    else:
        location_data = get_location(location)
        if location_data is None:
            return {
                "data": {
                    "Температура (°C)": "[НЕИЗВЕСТНО]",
                    "Влажность (%)": "[НЕИЗВЕСТНО]",
                    "Скорость ветра (км/ч)": "[НЕИЗВЕСТНО]",
                    "Вероятность дождя (%)": "[НЕИЗВЕСТНО]"
                },
                "name": "[НЕИЗВЕТСНО]",
                "good": False
            }

        location_key, localized_name = location_data

        data = get_weather_by_location(location_key)

    return {
        "data": dict(data.values()),
        "name": localized_name,
        "good": check_weather(data)
    }
