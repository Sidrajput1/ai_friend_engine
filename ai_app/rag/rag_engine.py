#from rag.retriever import retrieve_memories
#from rag.semantic_retriever import retrieve_memories
from rag.chroma_retriever import retrieve_memories
from persona.persona_manager import get_persona
from chat.conversation_summary import load_summary


def build_prompt(question,chat_history=None):

   
    
    persona = get_persona()

    #memories = retrieve_memories(question)

    #memory_text = "\n".join(memories) if memories else "No relevent long-term memory found"

    # add summary text too

    summary_text = load_summary()

    if not summary_text:
        summary_text = "No conversation summary availble"

    # store history of text
    history_text = ""
    if chat_history:
        for msg in chat_history[-6:]:   # min last 6 message only
            history_text += f"{msg['role']} : {msg['content']}\n"

    prompt = f"""
IMPORTANT:

You are Rahul.

You are the user's close friend.

Never say:

* I am an AI
* I am a chatbot
* I am a language model
* I don't have feelings
* As an AI

Always stay in character.

Always speak in Hinglish.

Always reply in 1-2 short sentences.

Never write long paragraphs.

Never sound like customer support.

Never break character.

---

Personality:
{persona['personality']}

Speaking Style:
{persona['style']}

Rules:
{persona['rules']}



Conversation Summary:
{summary_text}

Recent Conversation:
{history_text}

Current User Question:
{question}

Answer as Rahul.
Keep it short.
Keep it natural.
Keep it friendly.
"""

    print("\n===== FINAL PROMPT =====")
    print(prompt)
    print("========================\n")

    return prompt