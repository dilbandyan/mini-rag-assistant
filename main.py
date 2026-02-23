import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def load_knowledge():
    with open("knowledge.txt", "r") as f:
        text = f.read()
    # Split into sentences instead of paragraphs
    return [sentence.strip() for sentence in text.split(".") if sentence.strip()]


def retrieve(query, chunks, vectorizer, chunk_vectors):
    query_vector = vectorizer.transform([query])
    similarities = cosine_similarity(query_vector, chunk_vectors)[0]

    # Get top 2 most similar sentences
    top_indices = similarities.argsort()[-2:][::-1]
    return [chunks[i] for i in top_indices]


def generate_answer(context_sentences):
    return " ".join(context_sentences)


if __name__ == "__main__":
    print("Mini RAG Assistant (Improved Version)")

    chunks = load_knowledge()

    vectorizer = TfidfVectorizer()
    chunk_vectors = vectorizer.fit_transform(chunks)

    while True:
        query = input("\nYou: ")
        if query.lower() == "exit":
            break

        context = retrieve(query, chunks, vectorizer, chunk_vectors)
        answer = generate_answer(context)

        print("\nAI:", answer)