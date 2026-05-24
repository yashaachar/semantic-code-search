import numpy as np

class VectorStore:
    def __init__(self):
        self.vectors = []
        self.metadata = []

    def add(self, vector, meta):
        self.vectors.append(vector)
        self.metadata.append(meta)

    def search(self, query_vector, top_k=5):
        scores = []
        for i, vec in enumerate(self.vectors):
            score = self._cosine_similarity(query_vector, vec)
            scores.append((score, self.metadata[i]))
        scores.sort(reverse=True)
        return scores[:top_k]

    def _cosine_similarity(self, a, b):
        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))