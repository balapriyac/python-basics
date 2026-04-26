# Context-Aware Semantic Search with LLM Embeddings + Metadata Filtering

## What it covers
A simple semantic search engine over a ticket corpus. Uses `all-MiniLM-L6-v2` for embeddings, combines cosine similarity with metadata pre-filtering (team, status, priority, date range), and includes index persistence via NumPy + JSON.

## Who it's for
Developers building search, RAG pipelines, or any system where "find me relevant documents" needs to respect both meaning and structured constraints.

## Dependencies
```bash
pip install sentence-transformers numpy
```

## Key concepts
- Generating 384-dimensional embeddings locally, no API key
- Filter-before-score architecture and why it matters
- `min_score` threshold for suppressing noise results
- Persisting and reloading an index without re-encoding

