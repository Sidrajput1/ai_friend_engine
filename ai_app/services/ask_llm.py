import os
from services.ollama_service import ask_ollama
from services.llm_service import ask_gemini

#USE_OLLAMA = True


USE_OLLAMA = os.getenv("USE_OLLAMA", "true").lower() == "true"

def ask_llm(system_prompt, user_message):

    if USE_OLLAMA:
        return ask_ollama(
            system_prompt,
            user_message
        )

    return ask_gemini(
        system_prompt,
        user_message
    )

# def ask_llm(prompt, user_message=None):

# # OLD STYLE
#     if user_message is None:

#         if USE_OLLAMA:
#             return ask_ollama(
#             "",
#             prompt
#         )

#     return ask_gemini(prompt)


#     if USE_OLLAMA:
#         return ask_ollama(
#             prompt,
#             user_message
#         )

#     return ask_gemini(prompt)