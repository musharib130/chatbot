from langchain_core.messages import AIMessage
from ..state import ChatState
from ..llm import llm

def chatbot_node(state: ChatState):
    return {
        "messages": [AIMessage(llm.invoke(state["messages"]))]
    }
    
        