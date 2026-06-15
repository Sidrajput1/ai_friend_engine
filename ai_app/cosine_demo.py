from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

question = np.array([[1,2]])

memory_1 = np.array([[1, 2]])
memory_2 = np.array([[10, -5]])

print(
    cosine_similarity(question, memory_1)
)

print(
    cosine_similarity(question, memory_2)
)