def is_valid_memory(memory):

    invalid_phrases = [
        "not specified",
        "undefined",
        "unknown",
        "not mentioned",
        "cannot determine"
    ]

    memory_lower = memory.lower()

    for phrase in invalid_phrases:
        if phrase in memory_lower:
            return False

    return True