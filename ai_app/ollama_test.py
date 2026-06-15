# from services.ollama_service import ask_ollama

# response = ask_ollama(
#     "Explain React Hooks in simple words."
# )

# print(response)
# test_ollama.py

# from services.ollama_service import ask_ollama

# response = ask_ollama(
#     "My name is Sid. Reply in one line."
# )

# print(response)

## test_llm.py

from services.ask_llm import ask_llm

response = ask_llm(
    "Explain React Hooks in one sentence."
)

print(response)