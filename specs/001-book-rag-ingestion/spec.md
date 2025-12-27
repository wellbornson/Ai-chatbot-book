# Feature Specification: Book Content Ingestion & Embedding

**Feature Branch**: `001-book-rag-ingestion`  
**Created**: 2025-12-24  
**Status**: Draft  
**Input**: User description: "**Deploy book URLs, generate embeddings, and store them in a vector database** Target audience:** Developers integrating RAG with documentation websites Focus:** Reliable ingestion, embedding, and storage of book content for retrieval **Success criteria:** All public Docusaurus URLs are crawled and cleaned Text is chunked and embedded using Cohere models Embeddings are stored and indexed in Qdrant successfully Vector search returns relevant chunks for test queries **Constraints:** Tech stack: Python, Cohere Embeddings, Qdrant (Cloud Free Tier) Data source: Deployed Vercel URLs only Format: Modular scripts with clear config/env handling Timeline: Complete within 3-5 tasks **Not building:** Retrieval or ranking logic Agent or chatbot logic Frontend or FastAPI integration User authentication or analytics"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Ingest Documentation Site (Priority: P1)

As a developer, I want to run a pipeline that crawls my deployed documentation site and stores vector embeddings of the content, so that I can later search it semantically.

**Why this priority**: This is the core functionality (ETL pipeline) required to enable any RAG capabilities.

**Independent Test**: Configure the system with a target documentation URL and valid credentials, then execute the ingestion process. Verify it runs to completion and populates the database.

**Acceptance Scenarios**:

1. **Given** a valid Docusaurus base URL and API credentials, **When** the ingestion script is executed, **Then** all public pages are crawled, processed, and stored in the vector database.
2. **Given** an invalid or unreachable URL, **When** the ingestion script is executed, **Then** the system terminates with a descriptive error message.

---

### User Story 2 - Verify Embeddings via Search (Priority: P1)

As a developer, I want to run a simple test query against the stored data, so that I can verify the quality and retrieval of the embeddings.

**Why this priority**: Essential for validating that the ingestion process worked correctly and the data is usable.

**Independent Test**: Run a CLI command with a test query string and inspect the returned text chunks.

**Acceptance Scenarios**:

1. **Given** the database is populated with documentation content, **When** a search query for a known topic is executed, **Then** the system returns relevant text chunks from the original documentation.

---

### Edge Cases

- What happens when a page contains no extractable text? (Should be skipped or logged)
- How does the system handle rate limits from the embedding provider? (Should implement retry logic or fail gracefully)
- What happens if the crawler encounters a recursive link or infinite loop? (Should have depth/visited limits)
- How does the system handle duplicate content or pages? (Should dedup or overwrite based on URL)

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The system MUST crawl all public HTML pages starting from a provided base URL.
- **FR-002**: The system MUST extract main content text from HTML, removing navigation, footers, and script tags.
- **FR-003**: The system MUST split text content into manageable chunks suitable for embedding.
- **FR-004**: The system MUST generate vector embeddings for each text chunk using the configured model provider.
- **FR-005**: The system MUST store text chunks, metadata (URL, title), and embeddings in the vector database.
- **FR-006**: The system MUST provide a Command Line Interface (CLI) to trigger the ingestion process.
- **FR-007**: The system MUST provide a CLI utility to perform a similarity search query and display results.
- **FR-008**: The system MUST load configuration (URLs, API keys) from environment variables.

### Key Entities

- **Document Page**: Represents a single crawled URL and its raw HTML content.
- **Text Chunk**: A segment of text derived from a Document Page, containing the text payload, source URL, page title, and the vector embedding.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: 100% of publicly crawlable pages from the target documentation site are processed and indexed.
- **SC-002**: Ingestion pipeline completes for a standard 100-page site without manual intervention.
- **SC-003**: Search queries for specific technical terms defined in the documentation return the correct source chunk in the top 3 results.
- **SC-004**: System handles API rate limiting errors by pausing or retrying, ensuring 0% data loss during ingestion.

## Constraints & Assumptions

- **Tech Stack**: Python, Cohere Embeddings, Qdrant (Cloud Free Tier).
- **Data Source**: Deployed Vercel URLs (publicly accessible).
- **Scope**: No frontend, no complex ranking, no user auth.