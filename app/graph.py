from langgraph.graph import StateGraph, END
from langchain_core.messages import AIMessage
from .state import ChatState
from .llm import llm

def chatbot_node(state: ChatState):
    # Send full conversation to LLM
    response = llm.invoke(state["messages"])
    
    # Append LLM response to messages
    new_messages = state["messages"] + [AIMessage(response)]
    return {"messages": new_messages}

def build_graph():
    builder = StateGraph(ChatState)

    # Add a single chatbot node
    builder.add_node("chatbot", chatbot_node)
    builder.set_entry_point("chatbot")
    builder.add_edge("chatbot", END)

    return builder.compile()
