import logging
import asyncio
import uuid
import click
from storage import get_config, VectorStore
from crawler import fetch_url, parse_sitemap, extract_text
from processor import chunk_text, EmbeddingGenerator

def setup_logging(log_level="INFO"):
    logging.basicConfig(
        level=getattr(logging, log_level.upper(), logging.INFO),
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

async def run_ingestion(base_url, sitemap_path="/sitemap.xml", collection_name="documentation"):
    logging.info(f"Starting ingestion for {base_url}")
    
    # 1. Fetch and parse sitemap
    sitemap_url = base_url.rstrip("/") + sitemap_path
    try:
        sitemap_xml = await fetch_url(sitemap_url)
        urls = parse_sitemap(sitemap_xml)
        logging.info(f"Found {len(urls)} URLs in sitemap")
    except Exception as e:
        logging.error(f"Failed to fetch sitemap: {e}")
        return

    # 2. Setup services
    embedder = EmbeddingGenerator()
    store = VectorStore(collection_name=collection_name)
    store.ensure_collection()

    # 3. Process each URL
    for url in urls:
        try:
            logging.info(f"Processing {url}")
            html = await fetch_url(url)
            data = extract_text(html)
            
            if not data["text"].strip():
                logging.warning(f"No text extracted from {url}, skipping.")
                continue

            chunks = chunk_text(data["text"])
            logging.info(f"Generated {len(chunks)} chunks for {url}")

            # Generate embeddings (ideally in batches, but for simplicity one page at a time)
            embeddings = embedder.generate_embeddings(chunks)
            
            payloads = []
            for i, (chunk, vector) in enumerate(zip(chunks, embeddings)):
                payloads.append({
                    "id": str(uuid.uuid4()),
                    "vector": vector,
                    "metadata": {
                        "url": url,
                        "title": data["title"],
                        "text": chunk,
                        "chunk_index": i
                    }
                })
            
            store.upsert_chunks(payloads)
            logging.info(f"Successfully indexed {url}")
            
        except Exception as e:
            logging.error(f"Error processing {url}: {e}")
            # Continue to next URL

@click.group()
def cli():
    """Book Content Ingestion & Embedding CLI"""
    config = get_config()
    setup_logging(config.LOG_LEVEL)

@cli.command()
@click.argument("base_url")
@click.option("--sitemap", default="/sitemap.xml", help="Path to sitemap.xml")
@click.option("--collection", default="documentation", help="Qdrant collection name")
def ingest(base_url, sitemap, collection):
    """Crawl a documentation site and ingest its content."""
    asyncio.run(run_ingestion(base_url, sitemap, collection))

@cli.command()
@click.argument("query")
@click.option("--collection", default="documentation", help="Qdrant collection name")
@click.option("--limit", default=5, help="Number of results")
def search(query, collection, limit):
    """Search for relevant documentation snippets."""
    logging.info(f"Searching for: {query}")
    
    try:
        embedder = EmbeddingGenerator()
        store = VectorStore(collection_name=collection)
        
        query_vector = embedder.generate_query_embedding(query)
        results = store.search(query_vector, limit=limit)
        
        if not results:
            click.echo("No relevant documentation found.")
            return

        click.echo(f"\nFound {len(results)} relevant snippets:\n")
        for i, res in enumerate(results, 1):
            click.echo(f"--- Result {i} (Score: {res['score']:.4f}) ---")
            click.echo(f"Title: {res['title']}")
            click.echo(f"URL: {res['url']}")
            click.echo(f"Snippet: {res['text'][:300]}...")
            click.echo("")
            
    except Exception as e:
        logging.error(f"Search failed: {e}")
        click.echo(f"Error: {e}")

def main():
    cli()

if __name__ == "__main__":
    main()
