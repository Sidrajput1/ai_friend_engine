import numpy as np

from memory.memory_manager import load_memories
from memory.embedding_cache import load_cache, save_cache
from services.embedding_service import get_embedding

def cosine_similarity(vec1, vec2) -> float:
    a = np.array(vec1, dtype=float)
    b = np.array(vec2, dtype=float)

    denom = np.linalg.norm(a) * np.linalg.norm(b)
    if denom == 0:
        return 0.0

    return float(np.dot(a, b) / denom)


def retrieve_memories(question: str, top_k: int = 3, min_score: float = 0.25):
    memories = load_memories()
    if not memories:
        return []

    cache = load_cache()
    question_embedding = get_embedding(question)

    scored = []
    cache_changed = False

    for memory in memories:
        if memory not in cache:
            cache[memory] = get_embedding(memory)
            cache_changed = True

        score = cosine_similarity(question_embedding, cache[memory])
        scored.append((memory, score))

    if cache_changed:
        save_cache(cache)

    scored.sort(key=lambda item: item[1], reverse=True)

    relevant = [
        memory
        for memory, score in scored[:top_k]
        if score >= min_score
    ]

    return relevant

