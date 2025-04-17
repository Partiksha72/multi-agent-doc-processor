from langchain.tools import tool
from utils import query_groq_llm

@tool
def document_parser_tool(document: str) -> dict:
    sections = document.split("\n\n")
    structured = {}
    for i, sec in enumerate(sections):
        if sec.strip():
            section_key = f"Section_{i+1}"
            prompt = f"Extract the text and label this section according to the context of document in short:\n\n{sec}"
            structured[section_key] = query_groq_llm(prompt)
    return structured

