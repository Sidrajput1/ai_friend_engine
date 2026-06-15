def build_history_prompt(question, history):

    history_text = ""

    for msg in history:
        history_text += f"{msg['role']}: {msg['content']}\n"

    return f"""
You are Rahul.

Use ONLY the recent conversation below.

Conversation:
{history_text}

Question:
{question}

Answer using conversation only.

Speak HiEnglish
keep answer short
"""