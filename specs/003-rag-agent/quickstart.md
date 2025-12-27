# Quickstart: RAG Agent

## Prerequisites
- `backend/` initialized.
- `OPENAI_API_KEY` set in `.env` or `backend/.env`.
- `QDRANT_URL` and `QDRANT_API_KEY` set in `.env`.
- Python 3.14+ environment with `uv`.

## Installation

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Install dependencies:
   ```bash
   uv sync
   ```

## Usage

### Verify Installation
Check if the agent CLI is working:
```bash
uv run agent.py init
```

### Single Shot Question
Ask a specific question about the documentation:
```bash
uv run agent.py ask "How do I deploy Docusaurus?"
```

### Interactive Chat
Start a multi-turn conversation session:
```bash
uv run agent.py chat
```
You can type `exit` or `quit` to end the session.

### Resume Conversation
To resume a specific thread (useful for testing context):
```bash
uv run agent.py chat --thread-id "thread_abc123"
```