from langchain_core.messages import AIMessage
from ..state import ChatState
from ..llm import llm

async def chatbot_node(state: ChatState):
    # partial_response = ""
    for chunk in llm.stream(state["messages"]):
        # partial_response += chunk
         {
            "messages": [
                AIMessage(content=chunk)
            ]
        }