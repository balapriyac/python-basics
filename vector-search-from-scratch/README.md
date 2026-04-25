# Vector Search from Scratch in Python


## What it covers
Building a vector search engine using NumPy only — no external search libraries. Starts from scratch: simulated embeddings with cluster structure, a normalized index class, cosine similarity via dot product, and two matplotlib visualizations (PCA embedding space + score distribution).

## Who it's for
Developers who want to understand what a vector search engine actually does.

## Dependencies
```bash
pip install numpy matplotlib
```

## Key concepts
- L2 normalization and why it matters
- Cosine similarity as a dot product
- PCA projection for visualizing high-dimensional embeddings
- Score distribution and threshold intuition

## What it doesn't cover
Using embeddings from a pretrained model, metadata filtering, or index persistence. Those are covered in the companion article.
