from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from pdf_loader import load_pdfs

model = SentenceTransformer("all-MiniLM-L6-v2")

def retrieve_documents(query, top_k=3):
    documents = load_pdfs()

    texts = [d["text"] for d in documents]
    doc_ids = [d["doc_id"] for d in documents]

    query_emb = model.encode([query])
    doc_embs = model.encode(texts)

    scores = cosine_similarity(query_emb, doc_embs)[0]

    ranked = sorted(
        zip(doc_ids, texts, scores),
        key=lambda x: x[2],
        reverse=True
    )

    return [
        {
            "doc_id": doc_id,
            "score": round(float(score), 3),
            "preview": text[:300] + "..."
        }
        for doc_id, text, score in ranked[:top_k]
    ]
