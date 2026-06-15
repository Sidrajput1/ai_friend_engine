from vector_store.chroma_manager import search_memory

def retrieve_memories(question):

    results = search_memory(question)
    print("\n===== RETRIEVED MEMORIES =====")
    print(results["documents"][0])
    print("=============================\n")


    return results["documents"][0]