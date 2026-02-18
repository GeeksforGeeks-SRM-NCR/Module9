def retrieve(chunks, scores, top_k=3):

    indexed = list(zip(chunks, scores))

    indexed.sort(key=lambda x: x[1], reverse=True)

    return [i[0] for i in indexed[:top_k]]
