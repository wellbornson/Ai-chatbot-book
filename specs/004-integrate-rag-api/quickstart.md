# Quickstart: RAG API Integration

## Prerequisites
- Python 3.11+
- Node.js 18+
- Backend deps: `pip install fastapi uvicorn`

## Running the Backend
1. Navigate to root.
2. Run: `uvicorn backend.api:app --reload --port 8000`
3. Verify: `curl -X POST "http://localhost:8000/chat" -H "Content-Type: application/json" -d '{"query": "Hello"}'`

## Running the Frontend
1. Navigate to root.
2. Run: `npm start`
3. Frontend available at `http://localhost:3000`.
4. Chat widget should appear in bottom right.

## Troubleshooting
- **CORS Error**: Ensure `api.py` allows origin `http://localhost:3000`.
- **Import Error**: Ensure running uvicorn from *root* so `backend` module is found.
