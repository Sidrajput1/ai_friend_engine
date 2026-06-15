import json
#from services.llm_service import ask_llm
from services.ask_llm import ask_llm
def extract_memories(user_message):
#     prompt = f"""
# You are a memory extraction system.

# Extract only long-term facts about the user.

# Examples of facts:
# - Name
# - Profession
# - Skills
# - Preferences
# - Goals
# - Interests

# Do NOT extract:
# - Greetings
# - Temporary emotions
# - Casual conversation

# Message:
# "{user_message}"

# Return ONLY a valid JSON array.

# Example:
# [
#   "User name is Sidharth",
#   "User is a MERN developer"
# ]
# """

## acomment this prompt and adding new prompt

    # prompt = f"""
    # You are a memory extraction system.

    # Your job is to extract ONLY explicit facts that the user tells about themselves.

    # Examples of valid memories:


    # [
    # "User name is Sidharth",
    # "User is a MERN developer",
    # "User likes JavaScript",
    # "User wants to become a full-stack developer"
    # ]

    # Rules:

    # 1. Extract ONLY facts explicitly stated by the user.
    # 2. Do NOT guess.
    # 3. Do NOT infer.
    # 4. Do NOT answer questions.
    # 5. Do NOT create memories from questions.
    # 6. If the message contains no personal facts, return:

    # []

    # Examples:

    # Message:
    # "My name is Sidharth"

    # Output:
    # ["User name is Sidharth"]

    # Message:
    # "I am a MERN developer"

    # Output:
    # ["User is a MERN developer"]

    # Message:
    # "What is my name?"

    # Output:
    # []

    # Message:
    # "Hello"

    # Output:
    # []

    # Message:
    # "How are you?"

    # Output:
    # []

    # User Message:
    # "{user_message}"

    # Return ONLY a JSON array.
    # """

    prompt = f"""
TASK:

Extract long-term user facts.

Rules:

1. Return ONLY valid JSON.
2. Do NOT explain.
3. Do NOT talk.
4. Do NOT ask questions.
5. Do NOT add markdown.
6. Do NOT add code blocks.
7. If no memory exists return:

[]

Examples:

Input:
My name is Sidharth

Output:
["User name is Sidharth"]

Input:
I am a MERN developer

Output:
["User is a MERN developer"]

Input:
Hello

Output:
[]

Input:
What is my name?

Output:
[]

User Message:

{user_message}

Output:
"""

    response = ask_llm(prompt)
    print("\nGemini Raw Response:")
    print(response)

    response = response.replace("```json", "")
    response = response.replace("```", "")
    response = response.strip()

    try:
        memories = json.loads(response)
        return memories
    except Exception as e:
        print("Json error:",e)
        return []
