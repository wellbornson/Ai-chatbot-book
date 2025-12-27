# CLI Contract: Book Ingestion Pipeline

The system provides a CLI interface named `book-rag`.

## Commands

### `ingest`
Trigger the full ETL pipeline.

**Arguments**:
- `BASE_URL` (Required): The root URL of the Docusaurus site.

**Options**:
- `--sitemap-path`: Override default sitemap path (default: `/sitemap.xml`).
- `--collection-name`: Qdrant collection to target (default: `documentation`).
- `--dry-run`: Crawl and chunk without sending to Cohere or Qdrant.

**Example**:
```bash
python main.py ingest https://docs.example.com
```

### `search`
Perform a similarity search against the vector database.

**Arguments**:
- `QUERY` (Required): The text to search for.

**Options**:
- `--top-k`: Number of results to return (default: 5).
- `--collection-name`: Qdrant collection to search.

**Example**:
```bash
python main.py search "How do I configure sitemaps?"
```
