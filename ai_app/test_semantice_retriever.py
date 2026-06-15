from rag.semantic_retriever import retrieve_memories

questions = [
    "What is my name?",
    "What technology stack do I use?",
    "What is my goal?",
    "What language do I like?"
]

for q in questions:
    print("\nQUESTION:", q)
    print("MATCHES:", retrieve_memories(q))