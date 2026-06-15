import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key= os.getenv("GEMINI_API_KEY")
)

try:

        memories = [
            "User name is Sidharth",
            "User is a MERN developer",
            "User is learning Agentic AI",
            "User likes JavaScript",
           
        ]

        question = "What project am I building?"
        retrieved_memory = "User wants to build an AI Friend application"

        prompt = f"""
        Relevant Memory:
        {retrieved_memory}

        User Question:
        {question}

        Answer using the memory if relevant.
        """

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        print(response.text)
except Exception as e:
    print("An error occurred while generating content:")
    print(e)