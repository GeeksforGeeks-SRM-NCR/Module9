import numpy as np

def embed(texts):
    embeddings = model.encode(texts)
    return embeddings / np.linalg.norm(embeddings, axis=1, keepdims=True)
