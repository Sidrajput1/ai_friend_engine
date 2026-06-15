def classify_question(question):

    question = question.lower()

    history_keywords = [
        "what did i just say",
        "what were we talking about",
        "what happened earlier",
        "do you remember"
    ]

    memory_keywords = [
        "my goal",
        "my name",
        "my favorite language",
        "what technology stack"
    ]

    for keyword in history_keywords:
        if keyword in question:
            return "history"

    for keyword in memory_keywords:
        if keyword in question:
            return "memory"

    return "general"