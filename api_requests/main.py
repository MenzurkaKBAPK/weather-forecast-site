import requests

import json
import sys
import os

sys.path.append(os.getcwd())
from config import API_KEY


def get_location(location):
    response = requests.get(
        "https://dataservice.accuweather.com"
        "/locations/v1/cities/translate.json",
        params={
            "apikey": API_KEY,
            "q": location.lower(),
            "language": "ru-ru",
            "details": "true"
        }
    ).json()

    if response:
        return (
            response[0]["Key"], response[0]["LocalizedName"]
        )


def get_weather_by_location(location_key):
    response = requests.get(
        "https://dataservice.accuweather.com"
        f"/forecasts/v1/daily/1day/{location_key}",
        params={
            "apikey": API_KEY,
            "language": "ru-ru",
            "details": "true",
            "metric": "true"
        }
    )

    if response:
        data = response.json()

        temperature = (
            data["DailyForecasts"][0]["Temperature"]["Maximum"]["Value"]
        )
        humidity = (
            data["DailyForecasts"][0]["Day"]["RelativeHumidity"]["Average"]
        )
        wind_speed = (
            data["DailyForecasts"][0]["Day"]["Wind"]["Speed"]["Value"]
        )
        rain_probability = (
            data["DailyForecasts"][0]["Day"]["RainProbability"]
        )

        weather_data = {
            "temperature": ("Температура (°C)", temperature),
            "humidty": ("Влажность (%)", humidity),
            "wind_speed": ("Скорость ветра (км/ч)", wind_speed),
            "rain_prob": ("Вероятность дождя (%)", rain_probability)
        }

        return weather_data


def main():
    location_key, localized_name = get_location("Москва")
    if location_key:
        data = get_weather_by_location(location_key)

        print(f"Погода в городе {localized_name}:\n")
        to_len = max(map(lambda x: len(x[0]), data.values())) + 3
        answer = ""
        for name, value in data.values():
            answer += f"{name}{' ' * (to_len - len(name))}| {value}\n"
        print(answer, end="")

        with open("weather_data.json", "w") as file:
            json.dump(data, file)


if __name__ == "__main__":
    main()
