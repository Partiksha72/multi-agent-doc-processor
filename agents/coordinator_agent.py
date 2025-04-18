from langchain.tools import tool
import langsmith

@tool
def coordinator_agent(data: dict) -> str:
    """Coordinates between the agents to fetch the final summary"""
    with langsmith.start_trace("Coordinator_Agent_Trace"):
        result = "Coordinated workflow between agents."
        langsmith.log_input(f"Data received: {data}")
        langsmith.log_output(result)
    return result
