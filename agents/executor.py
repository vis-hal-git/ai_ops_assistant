# agents/executor.py
from tools.github_tool import github_search
from tools.weather_tool import get_weather
from tools.news_tool import get_news

TOOL_MAP = {
    "github_search": github_search,
    "get_weather": get_weather,
    "get_news": get_news
}

def executor_agent(state: dict):
    plan = state.get("plan", {"steps": []})
    results = []
    for step in plan["steps"]:
        tool_name = step["tool"]
        if tool_name in TOOL_MAP:
            tool_fn = TOOL_MAP[tool_name]
            results.append({
                "tool": tool_name,
                "output": tool_fn(**step["input"])
            })
    return {"data": results}
