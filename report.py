import json
import os

def generate_report(query, score, coverage, precision, recall, noise_ratio, explanation):
    status = "PASS" if score >= 60 else "FAIL"

    report = {
        "query": query,
        "score": score,
        "coverage": round(coverage * 100, 2),
        "precision": precision,
        "recall": recall,
        "noise_ratio": round(noise_ratio * 100, 2),
        "status": status,
        "explanation": explanation.strip()
    }

    os.makedirs("output", exist_ok=True)
    with open("output/audit_report.json", "w") as f:
        json.dump(report, f, indent=2)

    print("\n=== RETRIEVAL INTEGRITY AUDIT ===")
    for k, v in report.items():
        print(f"{k}: {v}")
