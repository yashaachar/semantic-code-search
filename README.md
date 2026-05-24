# 🔍 Semantic Code Search Engine

> Search your codebase using **natural language** — powered by sentence embeddings and custom vector similarity.

[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## Overview

Most code search tools rely on **keyword matching**. This engine understands **meaning**.

Type `"find files that sort arrays"` and it returns sorting algorithms — even if the word *"sort"* never appears in your code. Built on top of `sentence-transformers` with a **custom cosine similarity vector store** implemented from scratch — no FAISS, no shortcuts.

---

## ✨ Features

- 🧠 **Semantic understanding** — queries match by intent, not just keywords
- ⚡ **Fast local inference** — no API keys, no cloud calls
- 🏗️ **Custom vector store** — cosine similarity over NumPy, built from scratch
- 💾 **Persistent indexing** — SQLite stores snippet metadata between runs
- 🌐 **REST API** — clean FastAPI interface for indexing and searching

---

## Architecture

```
Query (natural language)
        │
        ▼
Sentence Embedder (all-MiniLM-L6-v2)
        │
        ▼
Vector Store (custom cosine similarity)
        │
        ▼
Top-K Ranked Results
```

| File | Responsibility |
|---|---|
| `embedder.py` | Converts code and queries into 384-dim vectors using `sentence-transformers` |
| `vector_store.py` | Custom O(n) cosine similarity search — no external vector DB |
| `database.py` | SQLite persistence for snippet metadata |
| `main.py` | FastAPI REST layer exposing `/index` and `/search` endpoints |

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.10+ |
| API | FastAPI + Uvicorn |
| Embeddings | sentence-transformers (`all-MiniLM-L6-v2`) |
| Vector Search | Custom cosine similarity (NumPy) |
| Storage | SQLite |

---

## Getting Started

### Prerequisites

- Python 3.10+
- pip

### Installation

```bash
git clone https://github.com/yashaachar/semantic-code-search
cd semantic-code-search

python -m venv venv

# Windows
venv\Scripts\activate

# Linux / Mac
source venv/bin/activate

pip install fastapi uvicorn sentence-transformers numpy
```

### Run

```bash
uvicorn main:app --reload
```

Server starts at **http://127.0.0.1:8000**

---

## API Reference

### Index a file

```http
POST /index?filepath=<path>
```

```bash
curl -X POST "http://127.0.0.1:8000/index?filepath=sample_code/sample1.py"
# {"message":"Indexed sample_code/sample1.py"}
```

### Search

```http
GET /search?query=<natural language query>&top_k=5
```

```bash
curl "http://127.0.0.1:8000/search?query=binary+search+algorithm"
# {"results":[{"score":0.7175,"file":"sample_code/sample1.py"},{"score":0.2042,"file":"sample_code/sample2.py"}]}
```

### Health Check

```http
GET /
```

---

## Search Results

| Query | Top Result | Score |
|---|---|---|
| `binary search algorithm` | sample1.py (Binary Search) | 0.7175 |
| `graph traversal BFS` | sample2.py (BFS/DFS) | 0.6061 |
| `sorting array divide and conquer` | sample4.py (Merge/Quick Sort) | 0.5049 |
| `stack push pop operations` | sample5.py (Stack/Queue) | 0.4181 |

---

## Project Structure

```
semantic-code-search/
├── main.py            # FastAPI app and API endpoints
├── embedder.py        # Sentence transformer embedding layer
├── vector_store.py    # Custom cosine similarity vector store
├── database.py        # SQLite metadata persistence
├── sample_code/
│   ├── sample1.py     # Binary Search, Linear Search
│   ├── sample2.py     # BFS, DFS (Graph Traversal)
│   ├── sample3.py     # Dynamic Programming, Memoization
│   ├── sample4.py     # Merge Sort, Quick Sort
│   └── sample5.py     # Stack, Queue implementations
└── README.md
```

---

## Key Design Decisions

**Why a custom vector store instead of FAISS?**
Built the cosine similarity search from scratch using NumPy to demonstrate a clear understanding of the underlying math — dot product normalization, vector space similarity — rather than abstracting it away behind a library.

**Why `all-MiniLM-L6-v2`?**
Fast, lightweight (~90MB), and produces strong 384-dimensional embeddings well-suited for semantic similarity tasks. Runs entirely locally with no API key required.

---

## Author

**Yasha V Achar**

[![GitHub](https://img.shields.io/badge/GitHub-yashaachar-181717?logo=github)](https://github.com/yashaachar)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?logo=linkedin)](https://linkedin.com/in/yashaachar)
