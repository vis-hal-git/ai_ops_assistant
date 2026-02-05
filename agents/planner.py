# agents/planner.py
from llm.openai_client import llm
import json

def planner_agent(state: dict):
    task = state.get("task", "")
    prompt = f"""
You are a Planner Agent.
Convert the task into tool steps.

ONLY return valid JSON.

Available tools:
- github_search(query)
- get_weather(city)
- get_news(topic)

Task: {task}

JSON Format:
{{
  "steps": [
    {{ "tool": "tool_name", "input": {{ }} }}
  ]
}}
"""
    response = llm.invoke(prompt)
    plan = json.loads(response.content)
    return {"plan": plan}
