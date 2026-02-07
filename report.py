import json
import os

def generate_report(query, analysis, score, noise_ratio):
    status = "PASS" if score >= 60 else "FAIL"

    report = {
        "query": query,
        "score": score,
        "coverage": round(analysis["coverage"] * 100, 2),
        "precision": analysis["precision"],
        "recall": analysis["recall"],
        "noise_ratio": round(noise_ratio * 100, 2),
        "status": status
    }

    # ✅ ALWAYS overwrite JSON file
    os.makedirs("output", exist_ok=True)
    with open("output/audit_report.json", "w") as f:
        json.dump(report, f, indent=2)

    # Console output
    print("\n=== RETRIEVAL INTEGRITY AUDIT ===")
    print(f"Query: {query}")
    print(f"Score: {score}/100")
    print(f"Coverage: {report['coverage']}%")
    print(f"Precision: {report['precision']}")
    print(f"Recall: {report['recall']}")
    print(f"Noise Ratio: {report['noise_ratio']}%")
    print(f"Status: {status}")
