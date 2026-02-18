import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize

def chunk_documents(documents):
    chunks = []

    for d in documents:
        sentences = sent_tokenize(d["text"])
        for s in sentences:
            chunks.append({"id": d["id"], "text": s})

    return chunks
