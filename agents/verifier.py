# agents/verifier.py
from llm.openai_client import llm

def verifier_agent(task, data):
    prompt = f"""
You are a Verifier Agent.
Validate and clean the output.

Task: {task}
Raw Data: {data}

Return a clean, structured final answer.
"""
    return llm.invoke(prompt).content
