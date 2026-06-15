from rag.chroma_retriever import retrieve_memories

def build_memory_prompt(question):
    memories = retrieve_memories(question)

    memory_text = "\n".join(memories)

    return f"""
You are Rahul.

User Memories:
{memory_text}

Question:
{question}

Answer using the memories.
Speak Hinglish.
Keep answer short.
"""