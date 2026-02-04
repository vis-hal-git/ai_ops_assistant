from langgraph.graph import StateGraph

def build_graph(planner, executor, verifier):
    graph = StateGraph(dict)

    graph.add_node("planner", planner)
    graph.add_node("executor", executor)
    graph.add_node("verifier", verifier)

    graph.set_entry_point("planner")
    graph.add_edge("planner", "executor")
    graph.add_edge("executor", "verifier")

    return graph.compile()
