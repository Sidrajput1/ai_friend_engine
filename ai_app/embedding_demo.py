import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

try:
    response = client.models.embed_content(
        model="text-embedding-004",
        contents="User is a MERN developer"
    )

    embedding = response.embeddings[0].values

    print(type(embedding))
    print(f"Vector Length: {len(embedding)}")
    print("\nFirst 10 Values:")
    print(embedding[:10])

except Exception as e:
    print("An error occurred while generating embeddings:")
    print(e)