from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from ..state import ChatState
from ..llm import get_llm
from ..tools.search import get_search

llm = get_llm()
search = get_search()

system_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You must ALWAYS use DuckDuckGo Search for any real-world query.
            Never answer from your internal knowledge or cached information.
            Do not output tool calls as text — call them directly.
            """
        ),
        MessagesPlaceholder(variable_name="messages")
    ]
)
tools = [search]

llm_with_tools = system_prompt | llm.bind_tools(tools=tools)

def chatbot_node(state: ChatState):
    res = llm_with_tools.invoke(state['messages'])
    
    # print(res)

    return {
        "messages": [res]
    }
    
        