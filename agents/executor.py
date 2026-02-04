# agents/executor.py
from tools.github_tool import github_search
from tools.weather_tool import get_weather
from tools.news_tool import get_news

TOOL_MAP = {
    "github_search": github_search,
    "get_weather": get_weather,
    "get_news": get_news
}

def executor_agent(plan):
    results = []
    for step in plan["steps"]:
        tool_fn = TOOL_MAP[step["tool"]]
        results.append(tool_fn(**step["input"]))
    return results
