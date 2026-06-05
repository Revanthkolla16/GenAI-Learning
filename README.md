# GenAI-Learning

A project-based journey through AI engineering — from raw API calls to multi-agent production systems.

This repo documents everything I build while learning the applied GenAI stack: LLM APIs, RAG pipelines, tool use, autonomous agents, multi-agent systems, and evals. No theory-only content — every folder is a working project.

**Stack:** Groq · Ollama · sentence-transformers · ChromaDB · LangChain · LangGraph · FastAPI · RAGAS · LangSmith

---

## Progress

| # | Project | Concepts | Status |
|---|---------|----------|--------|
| 01 | [Hello LLM](./01-hello-llm/) | Groq API, streaming, tokens | ✅|
| 02 | [Prompt playground](./02-prompt-playground/) | System prompts, temperature, prompt engineering | ✅|
| 03 | [Multi-turn CLI chatbot](./03-cli-chatbot/) | Conversation history, context window | ✅|
| 04 | [Semantic similarity explorer](./04-semantic-similarity/) | Embeddings, cosine similarity, sentence-transformers | 🔄|
| 05 | [Structured output extractor](./05-structured-outputs/) | JSON mode, output parsing | ⬜|
| 06 | [Personal notes search engine](./06-notes-search/) | Chunking, ChromaDB, vector search | ⬜|
| 07 | [PDF Q&A bot](./07-pdf-qa-bot/) | RAG pipeline, document loading | ⬜|
| 08 | [LLM with real tools](./08-llm-tools/) | Tool/function calling, tool loop | ⬜|
| 09 | [FastAPI RAG server](./09-fastapi-rag/) | REST API, /upload + /ask endpoints | ⬜|
| 10 | [Local LLM pipeline](./10-local-llm/) | Ollama, local inference, offline RAG | ⬜|
| 11 | [ReAct agent from scratch](./11-react-agent/) | ReAct loop, manual agent, no frameworks | ⬜|
| 12 | [Agent with memory](./12-agent-memory/) | LangGraph, short-term + long-term memory | ⬜|
| 13 | [Autonomous research agent](./13-research-agent/) | Planning, web search, LangGraph | ⬜|
| 14 | [GitHub PR review agent](./14-pr-review-agent/) | GitHub API, agentic code review | ⬜|
| 15 | [Coding agent with execution](./15-coding-agent/) | Code gen, subprocess sandbox, self-correction | ⬜|
| 16 | [Multi-agent debate system](./16-debate-agents/) | Multi-agent, supervisor pattern, LangGraph | ⬜|
| 17 | [Software engineering crew](./17-eng-crew/) | Planner + coder + reviewer agents | ⬜|
| 18 | [Agent with guardrails](./18-guardrails/) | Input validation, LLM-as-judge, safety | ⬜|
| 19 | [RAG eval harness](./19-rag-evals/) | RAGAS, faithfulness, relevance, correctness | ⬜|
| 20 | [Full-stack agentic app](./20-fullstack-agent/) | Streaming, LangSmith, FastAPI, frontend | ⬜|

---

## Why this repo exists

I’m a Final year CS undergrad at IIITDM Kancheepuram. This repo is my structured journey through AI engineering, which covers various topics like APIs, RAG pipelines, agents, multi-agent systems, and evaluation frameworks.

Each project is self-contained, runnable, and documented with what I learned.

---

## Setup

Most projects use a shared base. Clone the repo and set up once:

```bash
git clone https://github.com/Revanthkolla16/genai-learning
cd genai-learning
pip install groq langchain langgraph chromadb sentence-transformers fastapi uvicorn python-dotenv
```

Create a `.env` file in any project folder:

```env
GROQ_API_KEY=your_key_here
```

Get a free Groq API key at [console.groq.com](https://console.groq.com). No credit card needed.

---

## Contact

**Revanth Kolla** · [GitHub](https://github.com/Revanthkolla16) · revanthkolla23@gmail.com