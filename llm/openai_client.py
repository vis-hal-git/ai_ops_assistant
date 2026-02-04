import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load .env file
load_dotenv()

# Safety check (optional but recommended)
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY not found in environment")

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.3,
    api_key=os.getenv("OPENAI_API_KEY")
)
