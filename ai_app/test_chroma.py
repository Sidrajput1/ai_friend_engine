from vector_store.chroma_manager import add_memory
from vector_store.chroma_manager import search_memory
if __name__ == "__main__":
    add_memory("User is a MERN developer")

    print(
        search_memory(
            "What technology stack do I use?"
        )
    )