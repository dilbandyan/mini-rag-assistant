# Mini RAG Assistant (Offline Retrieval System)

A minimal Retrieval-Augmented Generation (RAG) style pipeline implemented in Python using TF-IDF vectorization and cosine similarity.

This project demonstrates the core concept behind retrieval-based AI systems without relying on external APIs.

---

## 🚀 Overview

This project simulates the retrieval component of a RAG system:

1. Load external knowledge base
2. Split knowledge into searchable units (sentences)
3. Convert text into vector representations (TF-IDF)
4. Convert user query into vector
5. Compute cosine similarity
6. Retrieve Top-K most relevant sentences
7. Generate response from retrieved context

Although no LLM is used, the architecture mirrors real-world RAG pipelines.

---

## 🧠 Architecture

Knowledge Base  
→ Sentence Splitting  
→ TF-IDF Vectorization  
→ Cosine Similarity Search  
→ Top-K Retrieval  
→ Response Generation  

This reflects the retrieval layer of modern AI systems.

---

## 🛠 Tech Stack

- Python
- NumPy
- Scikit-learn
- TF-IDF Vectorizer
- Cosine Similarity

---

## 📂 Project Structure

```
mini-rag-assistant/
│
├── main.py
├── knowledge.txt
├── requirements.txt
└── README.md
```

---

## ▶️ Run Locally

Install dependencies:

```bash
python3 -m pip install -r requirements.txt
```

Run the assistant:

```bash
python3 main.py
```

Type a question and press Enter.
Type `exit` to quit.

---

## 💬 Example Questions

- What is RAG?
- How does retrieval work?
- What are embeddings?
- What problem does RAG solve?
- What are RAG use cases?
- How does similarity search work?

---

## 🔍 How It Works (Technical Explanation)

- The knowledge base is split into sentences.
- Each sentence is converted into a TF-IDF vector.
- The user query is vectorized using the same vocabulary.
- Cosine similarity measures relevance between query and sentences.
- The Top-2 most similar sentences are returned as the response.

This mimics how embedding-based retrieval works in real RAG systems.

---

## 📈 Future Improvements

- Replace TF-IDF with embedding models
- Add vector database (FAISS / Pinecone)
- Integrate real LLM for answer synthesis
- Add similarity threshold filtering
- Add API interface

---

## 🎯 Purpose

Built as a portfolio project to demonstrate understanding of:

- Information retrieval
- Vector similarity
- Retrieval-Augmented Generation concepts
- NLP preprocessing
- Modular AI pipeline design
