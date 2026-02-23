from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from ..state import ChatState
from ..llm import get_llm
from ..tools import tools

llm = get_llm()

system_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a tool routing engine.

            Your ONLY job is to decide whether a tool must be called.

            RULES:

            - If external, real-world, or current information is required,
            call DuckDuckGo Search.

            - If the current UTC time is required,
            call the UTC time tool.

            - If no tool is required,
            return NOTHING.

            STRICT REQUIREMENTS:

            - DO NOT output JSON.
            - DO NOT output text.
            - DO NOT explain anything.
            - DO NOT wrap tool calls in text.
            - If calling a tool, use structured tool calling only.
            - If no tool is required, return an empty response.

            If the user says something like "hi", "hello", or casual text,
            DO NOT call any tool.
            """
        ),
        MessagesPlaceholder(variable_name="messages")
    ]
)

llm_with_tools = system_prompt | llm.bind_tools(tools=tools)

def intend_classifier(state: ChatState):
    res = llm_with_tools.invoke(state['messages'])
    
    return {
        "messages": [res]
    }
    
        