from rag.retriever import retrieve_memory

question = "What technology stack do I use?"

result = retrieve_memory(question)

print(result)
