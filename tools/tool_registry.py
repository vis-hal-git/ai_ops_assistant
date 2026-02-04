from tools.github_tool import github_search
from tools.weather_tool import get_weather
from tools.news_tool import get_news

# Central tool registry
TOOL_REGISTRY = {
    "github_search": {
        "fn": github_search,
        "description": "Search GitHub repositories by keyword"
    },
    "get_weather": {
        "fn": get_weather,
        "description": "Get current weather for a city"
    },
    "get_news": {
        "fn": get_news,
        "description": "Fetch latest news on a topic"
    }
}
