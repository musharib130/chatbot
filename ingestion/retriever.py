from langchain_chroma import Chroma
from ingestion.embedder import get_embedding_model

def get_retriever(persist_directory: str = "chroma_db"):
    embeddings = get_embedding_model()

    vectordb = Chroma(
        persist_directory=persist_directory,
        embedding_function=embeddings,
    )

    return vectordb.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 4}
    )