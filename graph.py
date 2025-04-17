from langgraph.graph import StateGraph
from langchain_core.runnables import RunnableLambda
from typing import TypedDict
from agents.document_parser import document_parser_tool
from agents.research_agent import verify_and_enrich
from agents.analysis_agent import analyze_content
from agents.summary_agent import generate_summary

class WorkflowState(TypedDict):
    document: str
    parsed: dict
    enriched: dict
    analyzed: dict
    summary: str

def build_graph():
    builder = StateGraph(state_schema=WorkflowState)
    def parse_step(state):
        parsed = document_parser_tool.invoke(state["document"])
        return {"parsed": parsed}

    def research_step(state):
        enriched = verify_and_enrich.invoke({"data": state["parsed"]})
        return {"enriched": enriched}

    def analyze_step(state):
        analyzed = analyze_content.invoke({"data": state["parsed"]})
        return {"analyzed": analyzed}

    def summary_step(state):
        summary = generate_summary.invoke({"data": state["parsed"]})
        return {"summary": summary}

    builder.add_node("parse", RunnableLambda(parse_step))
    builder.add_node("research", RunnableLambda(research_step))
    builder.add_node("analyze", RunnableLambda(analyze_step))
    builder.add_node("summarize", RunnableLambda(summary_step))

    builder.set_entry_point("parse")
    builder.add_edge("parse", "research")
    builder.add_edge("research", "analyze")
    builder.add_edge("analyze", "summarize")
    builder.set_finish_point("summarize")

    return builder.compile()



