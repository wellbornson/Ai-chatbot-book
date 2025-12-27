import sys
import os
import logging
from typing import Optional

# Ensure backend directory is in sys.path so that relative imports in agent.py work (e.g. from retrieve import ...)
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

# Import agent components
try:
    from agent import rag_agent, get_session
    from agents import Runner
except ImportError as e:
    logging.error(f"Failed to import agent: {e}")
    # Fallback or exit? For now, we allow app to start but endpoints might fail
    rag_agent = None

app = FastAPI(title="RAG Agent API", version="1.0.0")

# CORS Setup
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "https://book-chatbot-silk.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Models
class QueryRequest(BaseModel):
    query: str = Field(..., min_length=1, max_length=1000, description="User query text")
    thread_id: Optional[str] = Field(None, description="Conversation thread ID")

class QueryResponse(BaseModel):
    response: str
    thread_id: str
    status: str

# --- Auth System (Simple In-Memory for Demo) ---
users_db = {} # Format: {username: password}

class AuthRequest(BaseModel):
    username: str
    password: str

@app.post("/register")
def register(creds: AuthRequest):
    if creds.username in users_db:
        raise HTTPException(status_code=400, detail="User already exists")
    users_db[creds.username] = creds.password
    return {"status": "success", "message": "User registered successfully"}

@app.post("/login")
def login(creds: AuthRequest):
    if creds.username not in users_db or users_db[creds.username] != creds.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"status": "success", "token": f"fake-jwt-token-for-{creds.username}", "username": creds.username}
# -----------------------------------------------

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/chat", response_model=QueryResponse)
async def chat_endpoint(request: QueryRequest):
    if not rag_agent:
        raise HTTPException(status_code=500, detail="Agent not initialized")
    
    try:
        # Use provided thread_id or let get_session generate a new one?
        # get_session expects a thread_id. If None, we should generate one.
        import uuid
        thread_id = request.thread_id or str(uuid.uuid4())[:8]
        session = get_session(thread_id)
        
        result = await Runner.run(rag_agent, request.query, session=session)
        
        return QueryResponse(
            response=result.final_output,
            thread_id=thread_id,
            status="success"
        )
    except Exception as e:
        logging.error(f"Error processing query: {e}")
        raise HTTPException(status_code=500, detail=str(e))
