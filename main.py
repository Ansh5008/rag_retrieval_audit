import json
from retrieve import retrieve_documents
from analyze import analyze_retrieval
from evaluate import evaluate_retrieval
from score import calculate_score
from report import generate_report
from langchain_utils import extract_aspects, generate_explanation

# Load query
with open("data/queries.json") as f:
    q = json.load(f)

query_id = q["query_id"]
query = q["query"]

# Load ground truth
with open("data/ground_truth.json") as f:
    gt = json.load(f)

ground_truth = gt[query_id]

# LangChain: extract aspects
aspects = extract_aspects(query)

# Retrieve
retrieved = retrieve_documents(query)

# Analyze
relevant, noise, coverage = analyze_retrieval(retrieved, ground_truth)

# Evaluate
precision, recall = evaluate_retrieval(retrieved, ground_truth)

# Score
score, noise_ratio = calculate_score(coverage, len(noise), len(retrieved))

# LangChain: explanation
explanation = generate_explanation(query, coverage, noise_ratio)

# Report
generate_report(
    query,
    score,
    coverage,
    precision,
    recall,
    noise_ratio,
    explanation
)
