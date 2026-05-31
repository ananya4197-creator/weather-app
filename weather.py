# weather.py
import requests

API_KEY = "c5827a55f97952a37415c163034f4fbc"   # api key for OpenWeatherMap
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code == 200 and "main" in data:
        weather = {
            "city": data["name"],
            "temp": data["main"]["temp"],
            "desc": data["weather"][0]["description"].capitalize(),
            "humidity": data["main"]["humidity"],
            "wind": data["wind"]["speed"]
        }
        return weather
    else:
        return None