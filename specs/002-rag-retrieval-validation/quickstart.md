# Quickstart: RAG Retrieval Validation

## Prerequisites

- Python 3.14+
- `backend` directory initialized with `uv`
- `.env` file in `backend/` with `QDRANT_URL`, `QDRANT_API_KEY`, `COHERE_API_KEY`

## Installation

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```
2. Install dependencies (if not already done):
   ```bash
   uv sync
   ```

## Usage

### Basic Search

```bash
uv run retrieve.py "how to deploy docusaurus"
```

### Search with Limit

```bash
uv run retrieve.py "vector database" --limit 3
```

### Skip URL Validation

```bash
uv run retrieve.py "test" --no-validate
```

## Troubleshooting

- **Connection Error**: Check `.env` Qdrant credentials.
- **Auth Error**: Check Cohere API key.
- **Import Error**: Ensure you are running with `uv run` to use the virtual environment.
