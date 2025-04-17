# 🧠 Multi-Agent Document Processor using LangChain, LangGraph, Langsmith & Groq

This project implements a **modular, multi-agent system** that processes unstructured documents using LLMs. Each agent performs a specialized role—parsing, verifying/enriching, analyzing, and summarizing—coordinated through a LangGraph workflow. The system uses **Groq’s high-speed LLaMA-4 model** for inference.

---

## Features

- ✅ **Multi-agent architecture** using LangChain tools
- ✅ **Workflow orchestration** using LangGraph
- ✅ **High-performance LLM** queries via Groq
- ✅ **Structured document analysis & summarization**
- ✅ **Extensible and production-ready design**

---

## 🧰 Tech Stack

- **LangChain** – Tool & chain framework for LLMs
- **LangGraph** – Graph-based control over agent workflows
- **Groq API** – Access to LLaMA 4 for ultra-fast inference
- **Python** – Base language
- **LangSmith (Optional)** – For Logging and Security

---

## 📁 Project Structure
assignment/
├── agents/
│   ├── document_parser.py
│   ├── research_agent.py
│   ├── analysis_agent.py
│   ├── summary_agent.py
│   └── coordinator_agent.py
├── utils.py
├── graph.py
├── main.py
└── requirements.txt


---

## 🔧 Working

### 🛠 Step-by-Step Pipeline ✍️
### 1. utils.py – Groq LLM Wrapper
    -   Contains a helper function query_groq_llm(prompt: str) that interacts with Groq’s LLaMA model: All agents use this to send their prompt and receive a response. 

### 2. Agents (agents/ folder)
    -   Each agent is defined using the @tool decorator from LangChain, making them callable from the LangGraph workflow.

1. **Document Parser Agent : document_parser_tool** 🧩
    - Input: Raw document string.
    - Task: Splits document into sections and creates structured key-value pairs.
    - Output: Dict of structured sections.

2. **Research Agent : verify_and_enrich** 🧩
    - Input: Parsed content.
    - Task: Validates and enriches section content.
    - Output: Updated content dictionary with enriched info.

3. **Analysis Agent : analyze_content** 🧩
    - Input: Enriched sections.
    - Task: Performs deep analysis of each section using Groq.
    - Output: Dictionary with original + analysis.

4. **Summary Agent : generate_summary** 🧩
    - Input: Analyzed content.
    - Task: Summarizes and explains each section.
    - Output: String containing the full summarized report.

5. **Coordinator Agent : coordinator_agent** 🧩
    Input: Current graph state.
    Task: Controls the flow in LangGraph.
    Logic: Determines next step based on which part of the document state is missing.

### 3. graph.py – Graph Workflow Construction
    - Uses LangGraph to define a state machine-like workflow that moves through the following stages:  
                Input → Parse → Research → Analyze → Summarize → Output
    - Nodes are mapped to tools (agents), and an edge function determines the flow using the coordinator_agent.

### 4. main.py – 
 This script:
- Loads a document.
- Builds the agent workflow using LangGraph.
- Runs the graph with input.
- Prints the final summary.

---

## ▶️ How to Run

### 1. Install Dependencies

 - pip install -r requirements.txt
 - python main.py
 - User can upload file in this folder itself and change the file-name in main.py


