from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode, tools_condition

from .state import ChatState
from .agents.chatbot_node import chatbot_node, tools
from .nodes.retrieve import retrieve_node

tools_node = ToolNode(tools=tools)

TOOLS = 'tools'
CHATBOT = 'chatbot'
RETRIEVE = 'retrieve'

def should_continue(state: ChatState) -> str:
    last_message = state["messages"][-1]
    if last_message.tool_calls:
        return "tools"
    return "end"

def build_graph():
    builder = StateGraph(ChatState)

    # Add a single chatbot node 
    builder.add_node(CHATBOT, chatbot_node)
    builder.add_node(TOOLS, tools_node)
    builder.add_node(RETRIEVE, retrieve_node)

    builder.set_entry_point(RETRIEVE)
    builder.add_edge(RETRIEVE, CHATBOT)
    builder.add_edge(CHATBOT, END)

    # builder.add_conditional_edges(
    #     CHATBOT, 
    #     should_continue,
    #     {
    #         "tools": TOOLS,
    #         "end": END
    #     }
    # )

    # builder.add_edge(TOOLS, CHATBOT)

    return builder.compile()
