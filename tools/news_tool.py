# tools/news_tool.py
import requests, os

def get_news(topic: str):
    key = os.getenv("NEWS_API_KEY")
    url = f"https://newsapi.org/v2/everything?q={topic}&apiKey={key}"
    return requests.get(url).json()
