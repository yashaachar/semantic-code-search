Open `README.md` and replace everything with this:

```markdown
# Semantic Code Search Engine

> Search your codebase using natural language — powered by sentence embeddings and custom vector similarity.

---

## Overview

Most code search tools rely on keyword matching. This engine understands **meaning**.

Type `"find files that sort arrays"` and it returns sorting algorithms — even if the word "sort" never appears in your query. Built on top of sentence-transformers with a custom cosine similarity vector store implemented from scratch (no FAISS, no shortcuts).

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

**Components:**
- `embedder.py` — converts code and queries into 384-dim vectors using sentence-transformers
- `vector_store.py` — custom O(n) cosine similarity search, no external vector DB
- `database.py` — SQLite for persistent snippet metadata storage
- `main.py` — FastAPI REST layer exposing index and search endpoints

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.10+ |
| API | FastAPI + Uvicorn |
| Embeddings | sentence-transformers (all-MiniLM-L6-v2) |
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
venv\Scripts\activate        # Windows
source venv/bin/activate     # Linux/Mac
pip install fastapi uvicorn sentence-transformers numpy
```

### Run

```bash
uvicorn main:app --reload
```

Server starts at `http://127.0.0.1:8000`

---

## API Reference

### Index a file
```bash
POST /index?filepath=<path>
```
```bash
curl -X POST "http://127.0.0.1:8000/index?filepath=sample_code/sample1.py"
# {"message":"Indexed sample_code/sample1.py"}
```

### Search
```bash
GET /search?query=<natural language query>&top_k=5
```
```bash
curl "http://127.0.0.1:8000/search?query=binary+search+algorithm"
# {"results":[{"score":0.7175,"file":"sample_code/sample1.py"},{"score":0.2042,"file":"sample_code/sample2.py"}]}
```

### Health Check
```bash
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

**Why custom vector store instead of FAISS?**
Built the cosine similarity search from scratch using NumPy to demonstrate understanding of the underlying math — dot product normalization, vector space similarity — rather than abstracting it away with a library.

**Why all-MiniLM-L6-v2?**
Fast, lightweight (90MB), and produces strong 384-dim embeddings suitable for semantic similarity tasks. Runs locally with no API key required.

---

## Author

**Yasha V Achar** — [GitHub](https://github.com/yashaachar) · [LinkedIn](https://linkedin.com/in/yasha-v-achar)
```

