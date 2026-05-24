from fastapi import FastAPI
from embedder import embed
from vector_store import VectorStore
from database import init_db, insert_snippet
import os

app = FastAPI()
store = VectorStore()
conn = init_db()

@app.post("/index")
def index_file(filepath: str):
    with open(filepath, 'r') as f:
        code = f.read()
    vector = embed(code)
    snippet_id = len(store.vectors)
    insert_snippet(conn, filepath, code, "python")
    store.add(vector, {"id": snippet_id, "filename": filepath})
    return {"message": f"Indexed {filepath}"}

@app.get("/search")
def search(query: str, top_k: int = 5):
    query_vector = embed(query)
    results = store.search(query_vector, top_k)
    return {"results": [
        {"score": round(float(score), 4), "file": meta["filename"]}
        for score, meta in results
    ]}

@app.get("/")
def root():
    return {"message": "Semantic Code Search Engine is running"}