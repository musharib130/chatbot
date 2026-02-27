from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from ..state import ChatState
from ..llm import get_llm
from ..tools.search import get_search
from ..tools.current_time import current_time

llm = get_llm()
search = get_search()

system_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a research assistant with over 10 years of experience.

            Use the provided context to answer the question.
            If the answer is not in the context don't answer at all.
            Never answer from your own knowledge.

            Context:
            {context}
            """
        ),
        MessagesPlaceholder(variable_name="messages")
    ]
)

tools = [current_time, search]

llm_with_tools = system_prompt | llm

def chatbot_node(state: ChatState):
    res = llm_with_tools.invoke({
        "messages": state['messages'],
        "context": state["context"]
    })

    return {
        "messages": [res]
    }
    
        