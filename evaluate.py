def evaluate_retrieval(retrieved, ground_truth):
    retrieved_ids = set(d["doc_id"] for d in retrieved)
    gt_ids = set(ground_truth)

    tp = len(retrieved_ids & gt_ids)

    precision = tp / len(retrieved_ids)
    recall = tp / len(gt_ids)

    return round(precision, 2), round(recall, 2)
