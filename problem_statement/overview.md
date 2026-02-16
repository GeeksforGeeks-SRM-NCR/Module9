# Overview

This challenge focuses on building an accurate semantic file search system
using embedding-based retrieval.

The provided system implements a simplified Retrieval-Augmented pipeline:

1. Load local documents.
2. Split documents into smaller chunks.
3. Generate vector embeddings using a sentence-transformer model.
4. Compute similarity between a user query and document chunks.
5. Retrieve the most relevant results.

The system runs successfully but may produce inaccurate or misleading
retrieval results.

Participants must analyse the retrieval pipeline and improve its accuracy.
