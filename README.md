# 🤖 Agentic Notebooks (LangGraph + LangChain)

Hands-on Jupyter notebooks covering **agents**, **tool-calling**, and **RAG (Retrieval-Augmented Generation)** using LangGraph/LangChain with multiple vector store backends.

## 📑 Table of Contents
- [🏷️ Badges](#badges)
- [🖼️ Ecosystem Logos](#ecosystem-logos)
- [📌 What You’ll Find Here](#what-youll-find-here)
- [🗺️ Notebook Guide (Crisp Map)](#notebook-guide-crisp-map)
- [🔁 Visual: Corrective RAG Loop (High Level)](#visual-corrective-rag-loop-high-level)
- [🧰 Tech Stack (What’s Used)](#tech-stack-whats-used)
- [🚀 Quickstart (Local)](#quickstart-local)
- [📁 Data Folders](#data-folders)

## 🏷️ Badges
![Python](https://img.shields.io/badge/Python-3.12+-3776AB?logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-F37626?logo=jupyter&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-Framework-1C3C3C)
![LangGraph](https://img.shields.io/badge/LangGraph-Graphs-6E56CF)
![Groq](https://img.shields.io/badge/Groq-LLM%20API-000000)
![HuggingFace](https://img.shields.io/badge/Hugging%20Face-Embeddings-FFD21E?logo=huggingface&logoColor=000)
![Chroma](https://img.shields.io/badge/ChromaDB-Vector%20Store-6B4FBB)
![FAISS](https://img.shields.io/badge/FAISS-Vector%20Search-0467DF)
![Pinecone](https://img.shields.io/badge/Pinecone-Vector%20DB-0A0A0A)
![Tavily](https://img.shields.io/badge/Tavily-Web%20Search-2B6CB0)
![DuckDuckGo](https://img.shields.io/badge/DuckDuckGo-Search-DE5833?logo=duckduckgo&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-Validation-E92063?logo=pydantic&logoColor=white)

## 🖼️ Ecosystem Logos
| Tech | Logo | Link |
|---|---:|---|
| Hugging Face | <img height="28" alt="Hugging Face" src="https://unpkg.com/@lobehub/icons-static-svg@latest/icons/huggingface.svg" /> | https://huggingface.co |
| LangChain | <img height="28" alt="LangChain" src="https://unpkg.com/@lobehub/icons-static-svg@latest/icons/langchain.svg" /> | https://python.langchain.com |
| LangGraph | <img height="28" alt="LangGraph" src="https://unpkg.com/@lobehub/icons-static-svg@latest/icons/langgraph.svg" /> | https://langchain-ai.github.io/langgraph/ |
| LangSmith | <img height="28" alt="LangSmith" src="https://unpkg.com/@lobehub/icons-static-svg@latest/icons/langsmith.svg" /> | https://smith.langchain.com |
| AutoGen | <img height="28" alt="AutoGen" src="https://unpkg.com/@lobehub/icons-static-svg@latest/icons/autogen.svg" /> | https://microsoft.github.io/autogen/ |
| n8n | <img height="28" alt="n8n" src="https://unpkg.com/@lobehub/icons-static-svg@latest/icons/n8n.svg" /> | https://n8n.io |
| Agentic AI | <img height="28" alt="Agentic AI" src="https://raw.githubusercontent.com/twitter/twemoji/master/assets/svg/1f916.svg" /> | https://www.ibm.com/think/topics/agentic-ai |

## 📌 What You’ll Find Here
- Build blocks: prompts, chains, embeddings, loaders, and vector stores
- RAG: chunking → embedding → retrieval → generation
- Agent patterns: tool calling, routing, memory, and “corrective” retrieval loops

## 🗺️ Notebook Guide (Crisp Map)

### 🧩 LangGraph (agent graphs, tools, state)
| Notebook | What it covers | Key concepts |
|---|---|---|
| [langgraph_intro.ipynb](langgraph/langgraph_intro.ipynb) | First steps with StateGraph and state passing | Typed state, node functions, message/state updates |
| [langgraph_Agentic_Class_2.ipynb](langgraph/langgraph_Agentic_Class_2.ipynb) | Embeddings + Chroma retrieval wired into an agent-style state | HuggingFace embeddings, Chroma retriever, structured state |
| [langgrapha_Agentic_Class_3.ipynb](langgraph/langgrapha_Agentic_Class_3.ipynb) | Graph with and without tool calling | ToolNode, custom tools, message history, memory patterns |
| [langgraph_Agentic_Class_4.ipynb](langgraph/langgraph_Agentic_Class_4.ipynb) | Tool binding and tool selection behavior | bind_tools, inbuilt search tools, tool routing conditions |
| [tools.ipynb](langgraph/tools.ipynb) | Minimal custom tool examples | @tool, tool schemas, tool invocation |
| [Agentic RAG Class 5.ipynb](langgraph/Agentic%20RAG%20Class%205.ipynb) | End-to-end RAG from web content | Web loaders, splitting, embedding, retrieval, generation |
| [Corrective RAG Class 5.ipynb](langgraph/Corrective%20RAG%20Class%205.ipynb) | “Corrective RAG”: grade → rewrite → fallback search | Relevance grading, JSON parsing, query rewrite, web search fallback |
| [MultiAgent_Class_6.ipynb](langgraph/MultiAgent_Class_6.ipynb) | Advanced agent behaviors with tools (and demos) | ReAct-style agent usage, commands, tool execution, search/code tools |

### 🧱 LangChain (foundations, ingestion, vector DBs)
| Notebook | What it covers | Key concepts |
|---|---|---|
| [basics.ipynb](langchain/basics.ipynb) | Core LangChain building blocks | prompts, chains, model invocation, LangSmith env vars |
| [embeddings.ipynb](langchain/embeddings.ipynb) | Embedding text into vectors | HuggingFaceEmbeddings, vector dimensions, query vs doc embeddings |
| [data-ingestion.ipynb](langchain/data-ingestion.ipynb) | Loading documents from files | TextLoader, PDF loaders, lazy loading, document objects |
| [vectoredatabase.ipynb](langchain/FAISS/vectoredatabase.ipynb) | Vector similarity search + RAG with FAISS | cosine vs L2, FAISS indexing, retrieval, RAG patterns |
| [code.ipynb](langchain/Pinecone/code.ipynb) | Pinecone-backed vector store | index creation, upsert, query, PineconeVectorStore |

### ✅ Pydantic (structured outputs & validation)
| Notebook | What it covers | Key concepts |
|---|---|---|
| [pydantic.ipynb](pydantic/pydantic.ipynb) | Data validation vs plain dataclasses | BaseModel, type coercion, ValidationError, optional fields |

## 🔁 Visual: Corrective RAG Loop (High Level)
```mermaid
flowchart LR
  Q[User Question] --> R[Retrieve from Vector Store]
  R --> G[Grade Relevance]
  G -->|relevant| A[Answer with Context]
  G -->|irrelevant| W[Rewrite Query]
  W --> S[Web Search]
  S --> R
```

## 🧰 Tech Stack (What’s Used)
- LLMs: Groq (ChatGroq), optional Google GenAI integrations
- Embeddings: Sentence-Transformers via HuggingFaceEmbeddings
- Vector stores: ChromaDB, FAISS, Pinecone
- Search: Tavily, DuckDuckGo (ddgs)
- Parsing/validation: Pydantic (plus JSON output parsing patterns)
- Document ingestion: Text/PDF loaders (pypdf, pymupdf), BeautifulSoup (bs4)

## 🚀 Quickstart (Local)
1. Create a virtual environment and install deps:
   - `pip install -r requirements.txt`
2. Create a `.env` file (it is ignored by git) and set keys you plan to use:
   - `GROQ_API_KEY`
   - `HUGGINGFACE_API_KEY`
   - `TAVILY_API_KEY` (for Tavily search notebooks)
   - `PINECONE_API_KEY` (for Pinecone notebook)
   - `GOOGLE_API_KEY` (if using Google GenAI examples)
   - `LANGSMITH_API_KEY`, `LANGSMITH_PROJECT`, `LANGSMITH_TRACING_V2` (if tracing)
3. Open notebooks in Jupyter and run top-to-bottom.

## 📁 Data Folders
- [data/](data/) and [data2/](data2/) contain sample inputs used by some notebooks.
