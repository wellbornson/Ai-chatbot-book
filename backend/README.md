# Documentation RAG Ingestion Pipeline

This project provides an ETL pipeline to crawl Docusaurus documentation, generate vector embeddings, and store them in Qdrant for semantic search.

## Features
- Sitemap-based URL discovery.
- HTML cleaning and text extraction (BeautifulSoup4).
- Text chunking with overlap.
- Vector embeddings using Cohere `embed-english-v3.0`.
- Vector storage in Qdrant Cloud.
- CLI for ingestion and search.

## Setup

1.  Install [uv](https://github.com/astral-sh/uv).
2.  Install dependencies:
    ```bash
    uv sync
    ```
3.  Configure environment variables in `.env`:
    ```env
    COHERE_API_KEY=...
    QDRANT_URL=...
    QDRANT_API_KEY=...
    ```

## Usage

### Ingest Documentation
```bash
uv run main.py ingest https://your-docs-site.com
```

### Search Documentation
```bash
uv run main.py search "How do I install the CLI?"
```

## Testing
```bash
$env:PYTHONPATH="."
uv run pytest
```
