#utils.py
from sentence_transformers import SentenceTransformer
import numpy as np


def load_model(model_name="all-MiniLM-L6-v2"):
    return SentenceTransformer(model_name)


def cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))


def compute_sbert_scores(model, sentences1, sentences2):
    embeddings1 = model.encode(sentences1, convert_to_numpy=True)
    embeddings2 = model.encode(sentences2, convert_to_numpy=True)

    scores = []
    for v1, v2 in zip(embeddings1, embeddings2):
        scores.append(cosine_similarity(v1, v2))

    return scores