from langgraph.graph import StateGraph

from typing import TypedDict, List, Annotated
import operator

class AgentState(TypedDict):
    task: str
    plan: dict
    data: List[dict]
    final_answer: str

def build_graph(planner, executor, verifier):
    graph = StateGraph(AgentState)

    graph.add_node("planner", planner)
    graph.add_node("executor", executor)
    graph.add_node("verifier", verifier)

    graph.set_entry_point("planner")
    graph.add_edge("planner", "executor")
    graph.add_edge("executor", "verifier")
    graph.set_finish_point("verifier")

    return graph.compile()


