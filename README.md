# Mini RAG Assistant

A minimal Retrieval-Augmented Generation (RAG) pipeline implemented in Python.

## Overview

This project demonstrates a simple RAG workflow:

1. Load external knowledge base
2. Generate embeddings
3. Retrieve most relevant chunk
4. Pass context to LLM
5. Generate grounded response

## Tech Stack

- Python
- OpenAI Embeddings API
- Cosine Similarity (NumPy)

## Run

1. Install dependencies:

pip install -r requirements.txt

2. Set API key:

export OPENAI_API_KEY="your_key"

3. Run:

python main.py