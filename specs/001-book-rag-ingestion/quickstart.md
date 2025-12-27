# Quickstart: Book Ingestion Pipeline

## Prerequisites
- [uv](https://github.com/astral-sh/uv) installed.
- Cohere API Key.
- Qdrant Cloud Cluster + API Key.

## Setup

1.  Navigate to the backend directory:
    ```bash
    cd backend
    ```

2.  Create and configure `.env`:
    ```bash
    cp .env.example .env
    # Edit .env with your keys
    ```

3.  Install dependencies:
    ```bash
    uv sync
    ```

## Usage

### Run Ingestion
```bash
uv run main.py ingest https://your-docusaurus-site.vercel.app
```

### Test Search
```bash
uv run main.py search "What is the primary feature?"
```

## Testing
```bash
uv run pytest
```
