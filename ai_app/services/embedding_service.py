import json
from urllib import request

OLLAMA_EMBED_URL = "http://localhost:11434/api/embed"
EMBEDDING_MODEL = "nomic-embed-text-v2-moe"


def get_embedding(text: str) -> list[float]:
    payload = {
        "model": EMBEDDING_MODEL,
        "input": text
    }

    req = request.Request(
        OLLAMA_EMBED_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST"
    )

    with request.urlopen(req, timeout=60) as resp:
        data = json.loads(resp.read().decode("utf-8"))

    return data["embeddings"][0]