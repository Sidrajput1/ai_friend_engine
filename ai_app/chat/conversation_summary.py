import os
from dotenv import load_dotenv
from services.ask_llm import ask_llm

SUMMARY_FILE = os.path.join(os.path.dirname(__file__), "conversation_summary.txt")

def load_summary():
    if not os.path.exists(SUMMARY_FILE):
        return ""
    with open(SUMMARY_FILE, "r", encoding="utf-8") as file:
        return file.read().strip()


def save_summary(summary_text):
    with open(SUMMARY_FILE, "w", encoding="utf-8") as file:
        file.write(summary_text.strip())


def create_summary(old_messages, existing_summary=""):
    conversation_text = "\n".join(
        f"{msg['role']}: {msg['content']}" for msg in old_messages
    )

    prompt = f"""
You are a conversation summarizer.

Your task:
- Summarize the important context from the conversation below.
- Keep only useful facts, preferences, goals, emotional state, and important discussion points.
- Ignore greetings and repeated lines.
- Write in simple English.
- Keep the summary short but useful for future chat context.

Existing Summary:
{existing_summary}

New Conversation:
{conversation_text}

Return only the updated summary text. Do not use JSON.
"""

    return ask_llm(prompt)
