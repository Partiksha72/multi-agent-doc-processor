from langchain.tools import tool
from utils import query_groq_llm

@tool
def generate_summary(data: dict) -> str:
    summary = "--- SUMMARY OVERVIEW---\n\n"
    for section, content in data.items():
        brief = query_groq_llm(f"Summarize briefly:\n\n{content}")
        detail = query_groq_llm(f"Explain in detail:\n\n{content}")
        summary += f"{section}: {brief}\n\n--- Detail ---\n{detail}\n\n"
    return summary
