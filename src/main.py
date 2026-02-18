def chunk_documents(documents, chunk_size=300, overlap=50):
    chunks = []

    for d in documents:
        text = d["text"]
        start = 0

        while start < len(text):
            end = start + chunk_size
            chunk = text[start:end]
            chunks.append({"id": d["id"], "text": chunk})
            start += chunk_size - overlap

    return chunks
