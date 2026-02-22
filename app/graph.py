from langgraph.graph import StateGraph, END
from typing import TypedDict
from app.models import get_gpt_model
# from app.models import get_claude_model


class AgentState(TypedDict):
    input: str
    output: str


def llm_node(state: AgentState):
    model = get_gpt_model()  # Change to get_claude_model() if needed
    response = model.invoke(state["input"])
    return {"output": response.content}


def build_graph():
    builder = StateGraph(AgentState)

    builder.add_node("llm_node", llm_node)
    builder.set_entry_point("llm_node")
    builder.add_edge("llm_node", END)

    return builder.compile()
