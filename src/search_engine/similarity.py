import numpy as np

def similarity(query_vec, doc_vecs):

    
    scores = np.dot(doc_vecs, query_vec)

    return scores
