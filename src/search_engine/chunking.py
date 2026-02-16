def chunk_documents(documents):

    chunks = []

    for d in documents:

        text = d["text"]

        split = [text[:30], text[30:]]

        for s in split:
            chunks.append({"id":d["id"],"text":s})

    return chunks
