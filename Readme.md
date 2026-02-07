Retrieval Integrity Auditor for RAG Systems
==========================================

A retrieval-focused audit framework that evaluates the quality, completeness,
and trustworthiness of document retrieval in Retrieval-Augmented Generation
(RAG) pipelines. The goal is to validate evidence retrieval before answer
generation, so downstream responses are grounded in accurate and sufficient
context.

Why It Matters
--------------
RAG systems can look correct because language models are fluent, even when
retrieval is weak. Common hidden failures include:
- Missing critical evidence
- Irrelevant or noisy documents influencing answers
- Compliance and decision-making risks from incomplete evidence
- Over-reliance on top-1 similarity results

Core Capabilities
-----------------
- Coverage analysis against expected evidence
- Noise detection for irrelevant retrievals
- Ground-truth evaluation (precision and recall)
- Retrieval integrity scoring with clear PASS/FAIL logic
- Human-readable console output and JSON reporting

How It Works
------------
1. Load query and ground truth
2. Retrieve top-k documents via embeddings
3. Analyze coverage and noise
4. Evaluate precision and recall
5. Compute integrity score
6. Generate JSON and console reports

Project Structure
-----------------
rag_retrieval_audit/
|-- main.py                 # Orchestrates the full audit pipeline
|-- retrieve.py             # Semantic retrieval using embeddings
|-- analyze.py              # Coverage and noise analysis
|-- evaluate.py             # Precision and recall (ground truth)
|-- score.py                # Integrity score calculation
|-- report.py               # JSON + console report generation
|-- data/
|   |-- documents.json      # Knowledge base documents
|   |-- queries.json        # Input queries
|   |-- ground_truth.json   # Expected relevant documents
|-- output/
|   |-- audit_report.json   # Final audit output

Metrics
-------
Metric          Description
Coverage        % of required evidence retrieved
Precision       % of retrieved documents that are relevant
Recall          % of relevant documents retrieved
Noise Ratio     % of retrieved documents that are irrelevant
Integrity Score Overall retrieval quality (0-100)
Status          PASS / FAIL decision

Scoring and PASS/FAIL Logic
---------------------------
Integrity score is computed as:
- score = int((coverage * 70) - (noise_ratio * 30))

Decision rule:
- score >= 60 => PASS
- score < 60  => FAIL

A FAIL indicates retrieval quality is insufficient for safe generation, not
that the system is broken.

Data Format
-----------
documents.json
```json
[
  {
    "doc_id": "D1",
    "text": "GDPR defines rules for data protection and privacy in the EU."
  }
]
```

queries.json
```json
{
  "query_id": "q1",
  "query": "What is GDPR data retention policy for financial records?"
}
```

ground_truth.json
```json
{
  "q1": ["D1", "D2"]
}
```

Usage
-----
1. Install dependencies:
```bash
pip install sentence-transformers scikit-learn
```

2. Run the audit:
```bash
python main.py
```

Output
------
Console:
```text
=== RETRIEVAL INTEGRITY AUDIT ===
Query: What is GDPR data retention policy for financial records?
Score: 60/100
Coverage: 100.0%
Precision: 0.67
Recall: 1.0
Noise Ratio: 33.33%
Status: PASS
```

JSON report: output/audit_report.json
```json
{
  "query": "What is GDPR data retention policy for financial records?",
  "score": 60,
  "coverage": 100.0,
  "precision": 0.67,
  "recall": 1.0,
  "noise_ratio": 33.33,
  "status": "PASS"
}
```
