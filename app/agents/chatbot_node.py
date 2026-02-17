from langchain_core.messages import AIMessage
from ..state import ChatState
from ..llm import llm

def chatbot_node(state: ChatState):
    # Send full conversation to LLM
    response = llm.invoke(state["messages"])
    
    # Append LLM response to messages
    new_messages = state["messages"] + [AIMessage(response)]
    return {"messages": new_messages}