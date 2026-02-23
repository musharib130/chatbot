from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from rich.console import Console

from ..state import ChatState
from ..llm import get_llm

llm = get_llm()

console = Console()

system_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a assisstant, go through the available information in the context and summarize the information for me.
            """
        ),
        MessagesPlaceholder(variable_name="messages")
    ]
)

llm_with_tools = system_prompt | llm

def chatbot_node(state: ChatState):

    console.print(f"[bold red]state at chatnode =>[/bold red] {state}")

    res = llm_with_tools.invoke(state['messages'])
    
    return {
        "messages": [res]
    }
    
        