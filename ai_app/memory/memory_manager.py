import os
import json
from vector_store.chroma_manager import add_memory

# MEMORY_FILE = "memory_store.json"
BASE_DIR = os.path.dirname(__file__)

MEMORY_FILE = os.path.join(
    BASE_DIR,
    "memory_store.json"
)

def load_memories():
    with open(MEMORY_FILE,"r") as file:
        return json.load(file)


def save_memories(memory):
    memories = load_memories()
    if memory not in memories:
        memories.append(memory)
        
        add_memory(memory)

    with open(MEMORY_FILE,"w") as file:
        json.dump(memories,file, indent=4)


