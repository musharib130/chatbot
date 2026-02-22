from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode, tools_condition

from .state import ChatState
from .agents.chatbot_node import chatbot_node
from .agents.chatbot_node import tools

tools_node = ToolNode(tools=tools)

TOOLS = 'tools'
CHATBOT = 'chatbot'

def build_graph():
    builder = StateGraph(ChatState)

    # Add a single chatbot node
    builder.add_node(CHATBOT, chatbot_node)
    builder.add_node(TOOLS, tools_node)

    builder.set_entry_point(CHATBOT)
    
    builder.add_conditional_edges(
        CHATBOT, 
        tools_condition,
        {
            "tools": TOOLS,
            "__end__": END
        }
    )

    builder.add_edge(TOOLS, CHATBOT)

    return builder.compile()
