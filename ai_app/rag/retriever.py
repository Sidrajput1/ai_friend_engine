from memory.memory_manager import load_memories

def retrieve_memories(question):

    memories = load_memories()

    matched = []

    question = question.lower()

    for memory in memories:

        memory_lower = memory.lower()

        if "name" in question and "name" in memory_lower:
            matched.append(memory)

        if (
            "technology" in question
            or "stack" in question
            or "developer" in question
        ):
            if "developer" in memory_lower:
                matched.append(memory)

        if "language" in question:
            if "language" in memory_lower:
                matched.append(memory)

    return matched

# def retrieve_memory(question):
#     memories = load_memories()
#     # Simple retrieval logic - in a real application, you might use more sophisticated methods
#     #return [memory for memory in memories if question.lower() in memory.lower()]
#     question = question.lower()

#     for memory in memories:
#         memory_lower = memory.lower()
#         if(
#             "technology" in question
#             or "stack" in question
#             or "developer" in question
#         ):
#             if "developer" in memory_lower:
#                 return memory
        
#         if "name" in question:
#             if "name" in memory_lower:
#                 return memory
#     return None

        
