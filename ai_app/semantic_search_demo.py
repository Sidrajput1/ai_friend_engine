memories = [
    "User is a MERN developer",
    "User likes cricket",
    "User is learning Agentic AI",
    "User's name is Sidharth"
]

question = "What technology stack do I use?"

fake_similarity_scores = {
    "User is a MERN developer": 0.95,
    "User likes cricket": 0.12,
    "User is learning Agentic AI": 0.34,
    "User's name is Sidharth": 0.02
}

best_memory = max(
    fake_similarity_scores,
    key=fake_similarity_scores.get
)

print(best_memory)