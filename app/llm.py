from langchain_ollama import ChatOllama

def get_llm():
    return ChatOllama(
        model="mistral",  # change to your model name
        base_url="http://localhost:11434",
    )
