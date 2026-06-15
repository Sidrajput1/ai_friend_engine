from memory.memory_extractor import extract_memories
from memory.memory_manager import save_memories

message="""
My name is sidharth.
I am a MERN developer.
My favorite language is JavaScript.
I enjoy working on web applications.
I have a goal to become a full-stack developer.

"""
memories = extract_memories(message)
print("Extracted Memories:")
print(memories)

for memory in memories:
    save_memories(memory)


print("Done!")