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
- Precision and recall against ground truth
- Retrieval integrity scoring with PASS/FAIL logic
- LLM-based aspect extraction and explanations (via Ollama)
- Human-readable console output and JSON reporting

How It Works
------------
1. Load query and ground truth from `data/queries.json` and `data/ground_truth.json`
2. Extract query aspects with an LLM (currently not used in scoring)
3. Embed PDFs and the query with `all-MiniLM-L6-v2`
4. Retrieve top-k documents (default k=3)
5. Analyze coverage and noise
6. Evaluate precision and recall
7. Compute integrity score and PASS/FAIL status
8. Generate console output and `output/audit_report.json`

Project Structure
-----------------
rag_retrieval_audit/
|-- main.py                 # Orchestrates the full audit pipeline
|-- retrieve.py             # Semantic retrieval using embeddings
|-- pdf_loader.py           # Loads PDFs from data/pdfs
|-- analyze.py              # Coverage and noise analysis
|-- evaluate.py             # Precision and recall (ground truth)
|-- score.py                # Integrity score calculation
|-- report.py               # JSON + console report generation
|-- langchain_utils.py      # Aspect extraction + explanations (Ollama)
|-- data/
|   |-- queries.json        # Input query
|   |-- ground_truth.json   # Expected relevant documents
|   |-- pdfs/               # Knowledge base PDFs
|-- output/
|   |-- audit_report.json   # Final audit output

Metrics
-------
| Metric | Description | Range |
| --- | --- | --- |
| Coverage | % of ground-truth docs retrieved | 0-100 (percent in report) |
| Precision | True positives / retrieved docs | 0-1 |
| Recall | True positives / ground-truth docs | 0-1 |
| Noise Ratio | % of retrieved docs not in ground truth | 0-100 (percent in report) |
| Integrity Score | Weighted score | 0-70 |
| Status | PASS if score >= 60 | PASS/FAIL |

Scoring and PASS/FAIL Logic
---------------------------
Coverage and noise ratio are computed as fractions, then converted to percent
in the report. The score uses the fractional values:
- coverage_fraction = len(relevant) / len(ground_truth)
- noise_ratio_fraction = noise_count / total_retrieved
- score = int((coverage_fraction * 70) - (noise_ratio_fraction * 30))

Decision rule:
- score >= 60 => PASS
- score < 60  => FAIL

A FAIL indicates retrieval quality is insufficient for safe generation, not
that the system is broken.

Data Format
-----------
PDFs
Place source documents as PDFs in `data/pdfs/`. Each filename becomes a
`doc_id` used in retrieval and evaluation.

queries.json (single object)
```json
{
  "query_id": "q1",
  "query": "What is GDPR data retention policy for financial records?"
}
```

ground_truth.json
```json
{
  "q1": ["gdpr.pdf", "finance_rules.pdf"]
}
```

Setup
-----
1. Install dependencies:
```bash
pip install sentence-transformers scikit-learn pypdf langchain-community langchain-core
```

2. Install and run Ollama (required for aspect extraction and explanations):
```bash
ollama pull mistral
```

Usage
-----
Run the audit:
```bash
python main.py
```

If Ollama is not running, LLM steps will fail. You can swap the model or
disable LLM calls in `langchain_utils.py` if needed.

Output
------
Console:
```text
=== RETRIEVAL INTEGRITY AUDIT ===
query: What is GDPR data retention policy for financial records?
score: 60
coverage: 100.0
precision: 0.67
recall: 1.0
noise_ratio: 33.33
status: PASS
explanation: ...
```

JSON report: `output/audit_report.json`
```json
{
  "query": "What is GDPR data retention policy for financial records?",
  "score": 60,
  "coverage": 100.0,
  "precision": 0.67,
  "recall": 1.0,
  "noise_ratio": 33.33,
  "status": "PASS",
  "explanation": "..."
}
```
