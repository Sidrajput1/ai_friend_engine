from ollama import chat

# def ask_ollama(prompt):

#     response = chat(
#         model="llama3:latest",
#         messages=[
#             {
#                 "role": "user",
#                 "content": prompt
#             }
#         ]
#     )

#     return response.message.content

def ask_ollama(system_prompt, user_message):

    response = chat(
        model="llama3:latest",
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_message
            }
        ]
    )

    return response.message.content