import os
import time
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key = os.getenv("GEMINI_API_KEY")
)


messages = [
    {
        "role":"system",
        "content":"""
        You are Rahul.

        Personality:
        - supportive
        - funny

        Style:
        - Hinglish
        - use emojis

        Rules:
        - keep responses short
    """
    }
]




while True:
    user_input = input("\nyou: ")
    if user_input.lower() == "exit":
        print("goodbye tc ")
        break

    messages.append({
        "role":"user", 
        "content": user_input
        })
    

    prompt = ""

    print(f"Message Count: {len(messages)}")

    for message in messages:

        prompt += f"{message['role']} : {message['content']}\n"
        print("\n==============")
        print(prompt)
        print("==============\n")

    try:
        
        response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
        )

        ai_response = response.text
        messages.append({
        "role":"assistant",
        "content":ai_response
        })
        print(f"\nRahul: {ai_response}")
    # print("\n" + "=" * 50 + "\n")
    except Exception as e:
        # print("Error:", e)
        # print(type(e))
        # print(e)
        print("Model busy. Retrying in 5 seconds...")
        time.sleep(5)
        continue

    


# print(messages)

