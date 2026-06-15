from memory.memory_extractor import extract_memories
from memory.memory_manager import save_memories

from rag.rag_engine import build_prompt
from services.ask_llm import ask_llm
from memory.memory_validator import is_valid_memory
from chat.conversation_summary import load_summary , save_summary , create_summary
from prompts.generat_prompt import build_general_prompt

print("Your AI friend is ready to chat with you👉😊")
print("Type exit to quit.\n")

# adding chat history 

chat_history = []

while True:
    user_message = input("you: ")

    if(user_message.lower() == "exit"):
        break

    # 1) Save user message in chat history
    chat_history.append({
        "role": "user",
        "content": user_message
    })

    #step 2 : extract all memories

    memories = extract_memories(user_message)

    for memory in memories:
        # if "not specified" in memory.lower():
        #     continue

        # if "undefined" in memory.lower():
        #     continue

        # if "unknown" in memory.lower():
        #     continue
        if is_valid_memory(memory):
            save_memories(memory)
        
        # if chat gets too long , compress old message

        if len(chat_history) > 6:
            old_messages = chat_history[:4]
            recent_messages = chat_history[-4:]

            existing_summary = load_summary()
            new_summary = create_summary(old_messages, existing_summary)
            save_summary(new_summary)

            chat_history = recent_messages
    
    #step 3 build RAG prompt

    #prompt = build_prompt(user_message,chat_history)

    # add prompt from general prompt not into rag

    system_prompt = build_general_prompt(
        chat_history
    )

    #step -4 ask gemini ai or ollama

    #response = ask_llm(prompt)
    response = ask_llm(
    system_prompt,
    user_message
)

    print(f"\n AI friend :{response}\n")

     # 5) Save assistant response in chat history
    chat_history.append({
        "role": "assistant",
        "content": response
    })
