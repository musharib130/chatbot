from langchain_core.messages import AIMessage
from ..state import ChatState
from ..llm import get_llm
from ..tools.search import get_search

llm = get_llm()
search = get_search()

tools = [search]

llm_with_tools = llm.bind_tools(tools)

def chatbot_node(state: ChatState):
    return {
        "messages": [llm_with_tools.invoke(state["messages"])]
    }
    
        