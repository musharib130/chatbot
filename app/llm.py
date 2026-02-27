from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

def get_llm():
    return ChatOpenAI(
        model="gpt-4o-mini",  # or "gpt-4o", "gpt-4.1", etc.
        temperature=0,
        api_key=os.getenv("OPENAI_API_KEY"),
    )