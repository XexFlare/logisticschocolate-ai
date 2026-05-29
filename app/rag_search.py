from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

DOCS_DIR = Path(__file__).resolve().parents[1] / "docs"


def load_docs():
    docs = []
    for path in DOCS_DIR.glob("*.md"):
        docs.append({"title": path.name, "text": path.read_text(encoding="utf-8")})
    return docs


def search_docs(query: str, top_k: int = 2):
    docs = load_docs()
    if not docs or not query.strip():
        return []

    texts = [doc["text"] for doc in docs]
    vectorizer = TfidfVectorizer(stop_words="english")
    matrix = vectorizer.fit_transform(texts + [query])
    scores = cosine_similarity(matrix[-1], matrix[:-1]).flatten()

    ranked = sorted(zip(docs, scores), key=lambda x: x[1], reverse=True)[:top_k]
    return [
        {
            "title": doc["title"],
            "score": float(score),
            "excerpt": doc["text"][:700] + "...",
        }
        for doc, score in ranked
    ]
