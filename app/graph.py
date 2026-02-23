from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode, tools_condition

from .state import ChatState
from .agents.chatbot_node import chatbot_node
from .agents.intend_classifier import intend_classifier
from .tools import tools

tools_node = ToolNode(tools=tools)

TOOLS = 'tools'
CHATBOT = 'chatbot'
INTEND_CLASSIFIER = 'intend_classifier'

def should_continue(state: ChatState) -> str:
    last_message = state["messages"][-1]
    if last_message.tool_calls:
        return "tools"
    return "continue"

def build_graph():
    builder = StateGraph(ChatState)

    # Add a single chatbot node 
    builder.add_node(INTEND_CLASSIFIER, intend_classifier)
    builder.add_node(CHATBOT, chatbot_node)
    builder.add_node(TOOLS, tools_node)

    builder.set_entry_point(INTEND_CLASSIFIER)

    builder.add_conditional_edges(
        INTEND_CLASSIFIER, 
        should_continue,
        {
            "tools": TOOLS,
            "continue": CHATBOT
        }
    )

    builder.add_edge(TOOLS, CHATBOT)

    return builder.compile()
