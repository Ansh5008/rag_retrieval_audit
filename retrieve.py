import json
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

def retrieve_documents(query, top_k=3):
    with open("data/documents.json") as f:
        documents = json.load(f)

    doc_texts = [d["text"] for d in documents]

    query_emb = model.encode([query])
    doc_embs = model.encode(doc_texts)

    scores = cosine_similarity(query_emb, doc_embs)[0]

    ranked = sorted(
        zip(documents, scores),
        key=lambda x: x[1],
        reverse=True
    )

    retrieved = []
    for doc, score in ranked[:top_k]:
        retrieved.append({
            "doc_id": doc["doc_id"],
            "text": doc["text"],
            "score": round(float(score), 3)
        })

    return retrieved
