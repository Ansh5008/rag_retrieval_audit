🔍 Retrieval Integrity Auditor for RAG Systems

A retrieval-focused audit framework for evaluating the quality, completeness, and trustworthiness of document retrieval in Retrieval-Augmented Generation (RAG) pipelines.

This system evaluates retrieval quality independently of answer generation, ensuring that downstream LLM outputs are based on correct, complete, and low-noise evidence.

🚨 Why This Matters

RAG systems often appear correct because LLMs generate fluent answers.
However, retrieval failures are frequently hidden, leading to:

Missing critical evidence

Irrelevant or noisy documents influencing answers

Compliance and decision-making risks

Over-reliance on top-1 similarity results

This project addresses that gap by auditing retrieval before generation.

🎯 Core Objectives

Audit retrieved documents for coverage and relevance

Detect noise and irrelevant retrievals

Evaluate retrieval against ground truth evidence

Produce a retrieval integrity score (0–100)

Generate machine-readable and human-readable audit reports

Keep the system simple, explainable, and extensible

✨ Key Features
1️⃣ Coverage Analysis

Measures how much required evidence is retrieved

Detects incomplete or partial retrieval

Highlights potential missing evidence

2️⃣ Noise Detection

Identifies irrelevant or off-topic documents

Computes noise ratio and retrieval precision

Penalizes noisy retrieval behavior

3️⃣ Ground Truth Evaluation

Compares retrieved documents with labeled relevant documents

Computes:

Precision

Recall

Enables objective offline evaluation

4️⃣ Retrieval Integrity Scoring

Composite score (0–100) based on:

Coverage

Noise penalty

Clear PASS / FAIL gating logic

5️⃣ Explainable Reporting

Human-readable console output

Machine-readable JSON report

Clear justification for FAIL cases

🧠 What This System Is (and Is Not)
✅ This System IS

A retrieval quality auditor

Independent of LLM answer generation

Explainable and evaluation-driven

Suitable for enterprise RAG validation

❌ This System Is NOT

A chatbot

A trained ML model

A full production RAG platform

An answer generation engine

🗂️ Project Structure
rag_retrieval_audit/
│
├── main.py                 # Orchestrates the full audit pipeline
├── retrieve.py             # Semantic retrieval using embeddings
├── analyze.py              # Coverage and noise analysis
├── evaluate.py             # Precision & recall (ground truth)
├── score.py                # Integrity score calculation
├── report.py               # JSON + console report generation
│
├── data/
│   ├── documents.json      # Knowledge base documents
│   ├── queries.json        # Input queries
│   └── ground_truth.json   # Expected relevant documents
│
└── output/
    └── audit_report.json   # Final audit output

🔄 System Workflow
User Query
   ↓
Semantic Retrieval (Embeddings)
   ↓
Coverage & Noise Analysis
   ↓
Ground Truth Evaluation
   ↓
Integrity Scoring
   ↓
Audit Report (JSON + Console)

📊 Metrics Explained
Metric	Description
Coverage	% of required evidence retrieved
Precision	% of retrieved documents that are relevant
Recall	% of relevant documents retrieved
Noise Ratio	% of retrieved documents that are irrelevant
Integrity Score	Overall retrieval quality (0–100)
Status	PASS / FAIL decision
✅ PASS vs FAIL Logic
Score ≥ 60 → PASS (retrieval is trustworthy)
Score < 60 → FAIL (retrieval is risky)


A FAIL does not mean the system is broken.
It indicates retrieval quality is insufficient for safe generation.

📁 Data Format
documents.json
[
  {
    "doc_id": "D1",
    "text": "GDPR defines rules for data protection and privacy in the EU."
  }
]

queries.json
{
  "query_id": "q1",
  "query": "What is GDPR data retention policy for financial records?"
}

ground_truth.json
{
  "q1": ["D1", "D2"]
}

▶️ How to Run
1️⃣ Install Dependencies
pip install sentence-transformers scikit-learn

2️⃣ Run the Audit
python main.py

🧾 Sample Output (Console)
=== RETRIEVAL INTEGRITY AUDIT ===
Query: What is GDPR data retention policy for financial records?
Score: 60/100
Coverage: 100.0%
Precision: 0.67
Recall: 1.0
Noise Ratio: 33.33%
Status: PASS

📄 Sample Output (audit_report.json)
{
  "query": "What is GDPR data retention policy for financial records?",
  "score": 60,
  "coverage": 100.0,
  "precision": 0.67,
  "recall": 1.0,
  "noise_ratio": 33.33,
  "status": "PASS"
}