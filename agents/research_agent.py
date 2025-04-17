from langchain.tools import tool
from utils import query_groq_llm

@tool
def verify_and_enrich(data: dict) -> dict:
    enriched = {}
    for k, v in data.items():
        prompt = f"Verify and enrich this information:\n\n{v}"
        enriched[k] = query_groq_llm(prompt)
    return enriched
