import json
from retrieve import retrieve_documents
from analyze import analyze_retrieval
from score import calculate_score
from report import generate_report
from evaluate import evaluate_retrieval

# Load query
with open("data/queries.json") as f:
    q = json.load(f)

query_id = q["query_id"]
query = q["query"]

# Retrieve
retrieved = retrieve_documents(query)

# Load ground truth
with open("data/ground_truth.json") as f:
    gt = json.load(f)

ground_truth_ids = gt[query_id]

# Analyze
relevant, noise, coverage = analyze_retrieval(retrieved, ground_truth_ids)

# Score
score, noise_ratio = calculate_score(
    coverage,
    len(noise),
    len(retrieved)
)

# Evaluate
precision, recall = evaluate_retrieval(query_id, retrieved)

# Report
generate_report(
    query,
    {
        "coverage": coverage,
        "precision": precision,
        "recall": recall
    },
    score,
    noise_ratio
)
