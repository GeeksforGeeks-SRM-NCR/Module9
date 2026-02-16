# Semantic File Search Challenge (Level 100)

## Overview

This project implements a local semantic search system using embeddings.

Pipeline:

1. Load documents
2. Split into chunks
3. Generate embeddings using Sentence Transformers
4. Retrieve most relevant chunks for a query

The system runs successfully but contains subtle retrieval issues.

Participants must:

- Run the system
- Analyse retrieval behaviour
- Identify algorithmic flaws
- Improve retrieval accuracy


--------------------------------------------------

## Setup

Install dependencies:

pip install -r requirements.txt


--------------------------------------------------

## How to Run

python src/main.py


--------------------------------------------------

## Expected Behaviour

The system retrieves document chunks for a query.

Results may look reasonable but are often incorrect.

Participants must debug retrieval logic.


--------------------------------------------------

## Challenge Goals

- Understand embedding similarity
- Analyse ranking pipeline
- Improve semantic retrieval quality
