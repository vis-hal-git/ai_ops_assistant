# tools/github_tool.py
import requests
import os

def github_search(query: str):
    """Search for GitHub repositories."""
    url = f"https://api.github.com/search/repositories?q={query}"
    response = requests.get(url)
    if response.status_code == 200:
        items = response.json().get("items", [])
        return [{"name": item["full_name"], "url": item["html_url"], "stars": item["stargazers_count"]} for item in items[:5]]
    else:
        return {"error": f"GitHub API returned {response.status_code}"}
