import json

def evaluate_retrieval(query_id, retrieved_docs):
    with open("data/ground_truth.json") as f:
        ground_truth = json.load(f)

    true_docs = set(ground_truth[query_id])
    retrieved_ids = set(d["doc_id"] for d in retrieved_docs)

    true_positive = len(true_docs & retrieved_ids)

    precision = true_positive / len(retrieved_ids)
    recall = true_positive / len(true_docs)

    return round(precision, 2), round(recall, 2)
