# Agentic RAG with LangGraph

A robust **Corrective RAG (Retrieval-Augmented Generation)** pipeline implemented using **LangGraph** and **LangChain**.

## 🚀 Key Features
- **Self-Correction**: Grades retrieved documents for relevance.
- **Query Rewriting**: Rewrites queries if retrieved documents are irrelevant.
- **Web Search Fallback**: Uses DuckDuckGo search when local context is insufficient.
- **Visual Verbosity**: Detailed console logging for each node execution (Retrieve -> Grade -> Rewrite -> Search -> Generate).

## 🛠️ Tech Stack
- **Orchestration**: LangGraph, LangChain
- **Models**: Groq API (Llama3 / Qwen)
- **Vector Store**: ChromaDB
- **Search**: DuckDuckGo
