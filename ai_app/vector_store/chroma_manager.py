import chromadb
import uuid
from services.embedding_service import get_embedding

client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_or_create_collection(
    name="user_memories"
)

def add_memory(memory_text):

    embedding = get_embedding(memory_text)
    collection.add(
        documents=[memory_text],
       ids=[str(uuid.uuid4())],
        embeddings=[embedding]
    )


def search_memory(query):
    query_embedding = get_embedding(query)
    results = collection.query(
       # query_texts=[query],
       query_embeddings=[query_embedding],
        n_results=3
    )

    return results

# if __name__ == "__main__":
#     add_memory("User is a MERN developer")

#     print(
#         search_memory(
#             "What technology stack do I use?"
#         )
#     )

if __name__ == "__main__":

    add_memory("User is a MERN developer")
    add_memory("User likes JavaScript")
    add_memory("User wants to become a full-stack developer")

    results = search_memory(
        "What is my goal?"
    )

    print(results)