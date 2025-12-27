import click
import asyncio
import httpx
import logging
from dataclasses import dataclass
from typing import List, Optional
from storage import VectorStore
from processor import EmbeddingGenerator

@dataclass
class RetrievalResult:
    text: str
    score: float
    url: str
    title: str
    id: str = ""

@dataclass
class ValidationReport:
    query: str
    results_found: int
    top_score: float
    valid_urls: int
    status: str

def perform_search(query: str, limit: int = 5) -> List[RetrievalResult]:
    embedder = EmbeddingGenerator()
    store = VectorStore(collection_name="documentation")
    
    query_vector = embedder.generate_query_embedding(query)
    raw_results = store.search(query_vector, limit=limit)
    
    results = []
    for res in raw_results:
        results.append(RetrievalResult(
            text=res["text"],
            score=res["score"],
            url=res["url"],
            title=res["title"]
        ))
    return results

async def validate_urls(results: List[RetrievalResult]) -> int:
    valid_count = 0
    async with httpx.AsyncClient(timeout=10.0) as client:
        tasks = []
        for res in results:
            tasks.append(client.head(res.url, follow_redirects=True))
        
        responses = await asyncio.gather(*tasks, return_exceptions=True)
        
        for i, resp in enumerate(responses):
            if isinstance(resp, httpx.Response):
                try:
                    resp.raise_for_status()
                    valid_count += 1
                except Exception:
                    logging.warning(f"URL validation failed for {results[i].url}: Status {resp.status_code}")
            else:
                logging.warning(f"URL validation error for {results[i].url}: {resp}")
                
    return valid_count

def format_results(results: List[RetrievalResult], report: ValidationReport) -> str:
    output = []
    output.append("\nValidation Report:")
    output.append("------------------")
    output.append(f"Query: \"{report.query}\"")
    output.append(f"Status: {report.status}")
    output.append(f"Top Score: {report.top_score:.4f}")
    output.append(f"Valid URLs: {report.valid_urls}/{report.results_found}")
    output.append("\nResults:")
    
    for i, res in enumerate(results, 1):
        output.append(f"{i}. [{res.score:.4f}] {res.title} - {res.url}")
        output.append(f"   \"{res.text[:200]}...\"")
        output.append("")
        
    return "\n".join(output)

async def run_validation(query: str, limit: int, validate: bool):
    results = perform_search(query, limit=limit)
    
    valid_count = 0
    if validate:
        valid_count = await validate_urls(results)
    else:
        valid_count = len(results)
        
    top_score = results[0].score if results else 0.0
    # Logic for PASS: results found and (if validate is on, all must be valid)
    status = "PASS" if results and (not validate or valid_count == len(results)) else "FAIL"
    
    report = ValidationReport(
        query=query,
        results_found=len(results),
        top_score=top_score,
        valid_urls=valid_count,
        status=status
    )
    
    click.echo(format_results(results, report))

@click.command()
@click.argument("query")
@click.option("--limit", default=5, help="Number of results to return.")
@click.option("--validate/--no-validate", default=True, help="Whether to check URL reachability.")
def main(query, limit, validate):
    """Retrieve stored embeddings and validate the RAG retrieval pipeline."""
    # Setup minimal logging for warnings during validation
    logging.basicConfig(level=logging.WARNING, format='%(levelname)s: %(message)s')
    asyncio.run(run_validation(query, limit, validate))

if __name__ == "__main__":
    main()
