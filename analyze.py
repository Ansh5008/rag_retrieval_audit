def analyze_retrieval(retrieved_docs, ground_truth_ids):
    relevant = []
    noise = []

    for doc in retrieved_docs:
        if doc["doc_id"] in ground_truth_ids:
            relevant.append(doc)
        else:
            noise.append(doc)

    coverage = len(relevant) / len(ground_truth_ids)

    return relevant, noise, coverage
