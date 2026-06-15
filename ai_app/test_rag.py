from rag.rag_engine import build_prompt 

question = "What is my name?"

prompt = build_prompt(question)

print(prompt)