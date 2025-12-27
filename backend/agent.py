import click
import logging
import json
import os
import uuid
import asyncio
from agents import Agent, Runner, SQLiteSession, function_tool, OpenAIChatCompletionsModel
from retrieve import perform_search
from dotenv import load_dotenv, find_dotenv
from openai import AsyncOpenAI

# Load env from nearest .env file
load_dotenv(find_dotenv())

# Setup Logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# OpenRouter Configuration (as requested/detected in previous state)
ROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not ROUTER_API_KEY:
    logger.warning("OPENROUTER_API_KEY not found in environment variables.")
if not OPENAI_API_KEY:
    logger.warning("OPENAI_API_KEY not found in environment variables.")

client = AsyncOpenAI(
    api_key=ROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1",
)

third_party_model = OpenAIChatCompletionsModel(
    openai_client=client,
    model="mistralai/devstral-2512:free"
)

def search_knowledge_base_logic(query: str):
    """
    Core logic for searching the knowledge base.
    """
    logger.info(f"Searching knowledge base with query='{query}'")
    try:
        results = perform_search(query, limit=3)
        formatted_results = []
        for res in results:
            formatted_results.append(f"Title: {res.title}\nURL: {res.url}\nContent: {res.text[:500]}...")
        
        return "\n\n".join(formatted_results) if formatted_results else "No relevant information found."
    except Exception as e:
        logger.error(f"Search failed: {e}")
        return f"Error performing search: {str(e)}"

@function_tool
def search_knowledge_base(query: str) -> str:
    """
    Searches the internal knowledge base (books/docs) for relevant information.
    Use this for ANY question about technical documentation or book content.
    
    Args:
        query: The search query optimized for similarity search.
    """
    return search_knowledge_base_logic(query)

# Define the Agent
rag_agent = Agent(
    name="RAG Agent",
    instructions="You are a helpful assistant that answers questions about the provided book content. You MUST use the 'search_knowledge_base' tool to find information before answering. If the tool returns no results, state that you don't know.",
    tools=[search_knowledge_base],
    model=third_party_model,
)

def get_session(thread_id: str):
    if os.getenv("VERCEL"):
        # Vercel serverless functions have a read-only filesystem except for /tmp
        db_dir = "/tmp/.conversations"
    else:
        db_dir = ".conversations"
        
    os.makedirs(db_dir, exist_ok=True)
    db_path = f"{db_dir}/history.sqlite"
    return SQLiteSession(thread_id, db_path)

@click.group()
def cli():
    """RAG Agent CLI (OpenAI Agents SDK Edition)"""
    pass

@cli.command()
def init():
    """Verify agent configuration."""
    click.echo(f"Agent '{rag_agent.name}' initialized with tools: {[t.name for t in rag_agent.tools]}")

@cli.command()
@click.argument("question")
@click.option("--thread-id", default=None, help="Resume conversation from this ID.")
def ask(question, thread_id):
    """Ask a single question."""
    async def main():
        tid = thread_id or str(uuid.uuid4())[:8]
        session = get_session(tid)
        
        result = await Runner.run(rag_agent, question, session=session)
        
        click.echo(result.final_output)
        if not thread_id:
            click.echo(f"\n[Session ID: {tid}]")
            
    asyncio.run(main())

@cli.command()
@click.option("--thread-id", default=None, help="Resume conversation from this ID.")
def chat(thread_id):
    """Interactive chat session."""
    async def main():
        tid = thread_id or str(uuid.uuid4())[:8]
        session = get_session(tid)
        
        click.echo(f"Starting chat (Session ID: {tid})")
        
        while True:
            try:
                user_input = await asyncio.to_thread(click.prompt, "You")
                if user_input.lower() in ['exit', 'quit']:
                    break
                
                result = await Runner.run(rag_agent, user_input, session=session)
                click.echo(f"Agent: {result.final_output}")
                
            except KeyboardInterrupt:
                break
            except Exception as e:
                click.echo(f"Error: {e}")
                
    asyncio.run(main())

if __name__ == "__main__":
    cli()