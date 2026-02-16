from utils.data_loader import load_documents
from search_engine.chunking import chunk_documents
from search_engine.embedding import embed
from search_engine.similarity import similarity
from search_engine.retrieval import retrieve

documents = load_documents("data/documents.json")

chunks = chunk_documents(documents)

texts = [c["text"] for c in chunks]

embeddings = embed(texts)

query = "machine learning"

query_vec = embed([query])[0]

scores = similarity(query_vec, embeddings)

results = retrieve(chunks, scores)

print("Retrieved Chunks:")
for r in results:
    print(r)
