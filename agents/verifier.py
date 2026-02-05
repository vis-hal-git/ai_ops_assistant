# agents/verifier.py
from llm.openai_client import llm

def verifier_agent(state: dict):
    task = state.get("task", "")
    data = state.get("data", [])
    prompt = f"""
You are a Verifier Agent.
Validate and clean the output.

Task: {task}
Raw Data: {data}

Return a clean, structured final answer.
"""
    final_answer = llm.invoke(prompt).content
    return {"final_answer": final_answer}
