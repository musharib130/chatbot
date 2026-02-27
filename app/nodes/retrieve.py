# graph/nodes/retrieve.py

from langchain_core.documents import Document
from ..state import ChatState
from ingestion.retriever import get_retriever

retriever = get_retriever()

def retrieve_node(state: ChatState):
    user_message = state["messages"][-1].content

    docs: list[Document] = retriever.invoke(user_message)

    # Combine documents into single context string
    context = "\n\n".join([doc.page_content for doc in docs])

    return {
        "context": context
    }