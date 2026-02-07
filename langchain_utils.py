import json
from langchain_community.llms import Ollama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = Ollama(model="mistral")

# -------- Aspect Extraction --------
aspect_prompt = PromptTemplate.from_template("""
Extract the key aspects required to answer the following query.
Return ONLY a JSON list.

Query: {query}
""")

aspect_chain = aspect_prompt | llm | StrOutputParser()

def extract_aspects(query):
    response = aspect_chain.invoke({"query": query})
    try:
        return json.loads(response)
    except:
        return []

# -------- Explanation Generation --------
explain_prompt = PromptTemplate.from_template("""
Explain in simple language why the retrieval quality is good or bad.

Query: {query}
Coverage: {coverage}
Noise Ratio: {noise_ratio}
""")

explain_chain = explain_prompt | llm | StrOutputParser()

def generate_explanation(query, coverage, noise_ratio):
    return explain_chain.invoke({
        "query": query,
        "coverage": coverage,
        "noise_ratio": noise_ratio
    })
