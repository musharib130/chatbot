from langgraph.graph import StateGraph, END
from .state import ChatState
from .agents.chatbot_node import chatbot_node

def build_graph():
    builder = StateGraph(ChatState)

    # Add a single chatbot node
    builder.add_node("chatbot", chatbot_node)
    builder.set_entry_point("chatbot")
    builder.add_edge("chatbot", END)

    return builder.compile()
