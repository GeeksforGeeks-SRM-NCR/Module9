def similarity(query_vec, doc_vecs):
    query_vec = query_vec / np.linalg.norm(query_vec)
    doc_vecs = doc_vecs / np.linalg.norm(doc_vecs, axis=1, keepdims=True)
    return np.dot(doc_vecs, query_vec)
