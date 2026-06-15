from rag.rag_engine import build_prompt
from services.llm_service import ask_llm

question = "What technology stack do I use?"

try:

    prompt = build_prompt(question)

    response = ask_llm(prompt)

    print(response)
except Exception as e:
    print(f"Error: {e}")