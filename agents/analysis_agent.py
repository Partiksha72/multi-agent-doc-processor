from langchain.tools import tool
from utils import query_groq_llm

@tool
def analyze_content(data: dict) -> dict:
    """Performs deep analysis of content using Groq."""
    analysis = {}
    for k, v in data.items():
        prompt = f"Analyze the following section deeply:\n\n{v}"
        analysis[k] = {
            "original": v,
            "analysis": query_groq_llm(prompt)
        }
    return analysis
