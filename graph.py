
from langgraph.graph import StateGraph, START, END

from state import AgentState
from nodes.planning import planning_node
from nodes.architect import architect_node
from nodes.coder import coder_node


def build_graph():
    workflow = StateGraph(AgentState)

    workflow.add_node("planner", planning_node)
    workflow.add_node("architect", architect_node)
    workflow.add_node("coder", coder_node)

    workflow.add_edge(START, "planner")
    workflow.add_edge("planner", "architect")
    workflow.add_edge("architect", "coder")
    workflow.add_edge("coder", END)

    return workflow.compile()


agent = build_graph()
