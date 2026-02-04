# tools/weather_tool.py
import requests, os

def get_weather(city: str):
    key = os.getenv("WEATHER_API_KEY")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}"
    return requests.get(url).json()
