import os

from dotenv import load_dotenv
from google import genai
from persona_template import personal
# from dotenv import load_dotenv
# from openAI import openAI

load_dotenv()

client = genai.Client(
    api_key = os.getenv("GEMINI_API_KEY")
)

#model = genai.GenerativeModel("gemini-1.5-flash-latest")

# response = client.models.generate_content(
#     model="gemini-2.5-flash",
#     contents = """
#    You are a funny friend who teaches coding.
# Explain React hooks to a beginner.
#     """
# )

# print(response.text)


# client = openAI(
#     api_key=os.getenv("GEMINI_API_KEY"),
#     base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
# )

# response = client.chat.completions.create(
#     model="gemini-1.5-flash-latest",
#     prompt = """
# You are a senior MERN developer.

# Explain React hooks to a beginner.
# """
# )

# print(response.choices[0].message.content);


