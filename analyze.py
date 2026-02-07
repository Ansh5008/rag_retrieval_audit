def analyze_retrieval(retrieved, ground_truth):
    relevant = []
    noise = []

    for doc in retrieved:
        if doc["doc_id"] in ground_truth:
            relevant.append(doc)
        else:
            noise.append(doc)

    coverage = len(relevant) / len(ground_truth)
    return relevant, noise, coverage
