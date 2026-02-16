from langchain_ollama import OllamaLLM

llm = OllamaLLM(
    model="mistral",  # change to your model name
    base_url="http://localhost:11434",
)
