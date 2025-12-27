# Research: Book Content Ingestion & Embedding

## Decision: Docusaurus Crawling Strategy
**Decision**: Use `sitemap.xml` for URL discovery.
**Rationale**: Docusaurus automatically generates a `sitemap.xml`. This is more reliable and faster than recursive HTML crawling.
**Alternatives considered**: Recursive link following (slower, risk of loops), parsing `sidebars.js` (complex, requires JS environment).

## Decision: Text Extraction Patterns
**Decision**: Target `<article>` or `.theme-doc-markdown` tags using BeautifulSoup4.
**Rationale**: Docusaurus wraps main content in specific semantic tags. This minimizes noise from sidebars and headers.
**Alternatives considered**: Generic text extraction (too much noise), Readability.js (overkill for simple documentation).

## Decision: Embedding Model & Chunking
**Decision**: Cohere `embed-english-v3.0` with 512-token chunks and 10% overlap.
**Rationale**: Cohere V3 models handle 512 tokens natively and are optimized for RAG. 10% overlap preserves context across boundaries.
**Alternatives considered**: `embed-english-light-v3.0` (faster but less accurate).

## Decision: Vector Database Configuration
**Decision**: Qdrant with Cosine Similarity, 1024 dimensions (for Cohere v3).
**Rationale**: Cohere `embed-english-v3.0` outputs 1024 dimensions. Cosine similarity is the recommended metric for these embeddings.
**Alternatives considered**: Euclidean distance (less effective for high-dimensional embeddings).

## Decision: Project Management
**Decision**: Use `uv` for Python environment and dependency management.
**Rationale**: `uv` is extremely fast and provides reproducible environments with a single tool.
**Alternatives considered**: `poetry` (slower), `venv` + `pip` (less robust for dependency locking).
