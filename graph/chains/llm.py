# graph/chains/llm.py
import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

def get_llm(max_tokens: int = 1024) -> ChatOpenAI:
    return ChatOpenAI(
        model="gpt-4o-mini",
        openai_api_key=os.environ["OPENAI_API_KEY"],
        temperature=0.1,
        max_tokens=max_tokens,
        max_retries=3,
    )