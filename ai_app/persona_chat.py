persona={
     "name": "Rahul",
    "personality": "supportive and funny",
    "style": "Hinglish with emojis",
    "rules": "Keep replies short"
}

persona_prompt = f"""
    you are {persona["name"]}
    personality is {persona["personality"]}
    speaking style is {persona['style']}
    rules to follow {persona['rules']}
"""

chat_history = [
    {
        "role": "user",
        "content" : "Hi rahul"

    },

    {
        "role": "assistant",
        "content" : "hey bro 😊"
    }
]

current_message = "i failed my interview!"

# print(persona_prompt)
history_text= " "

for message in chat_history:
   history_text+=f"{message['role']} : {message['content']}\n"

final_prompt = f"""
    {persona_prompt}

conversation_history = {history_text}

current_user_message: {current_message}

respond as rahul, keeping in mind the personality, style and rules mentioned above.
"""

print(final_prompt)