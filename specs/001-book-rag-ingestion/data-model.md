# Data Model: Book Content Ingestion

## Entities

### DocumentPage
Represents a single source page from the documentation.

| Field | Type | Description |
|-------|------|-------------|
| url | String | The absolute URL of the page (Unique identifier) |
| title | String | The page title (usually from H1) |
| raw_text | String | The cleaned text content of the page |

### TextChunk
Represents a vector-indexed segment of a DocumentPage.

| Field | Type | Description |
|-------|------|-------------|
| id | UUID | Unique identifier for the chunk |
| doc_url | String | Reference to the source DocumentPage |
| doc_title | String | Title of the source page |
| text | String | The text segment content |
| vector | List[Float] | The 1024-dimensional embedding |
| chunk_index | Integer | The sequence number of the chunk within the page |

## Relationships
- A `DocumentPage` has many `TextChunk`s.
- `TextChunk` contains metadata to link back to the source URL without requiring a separate SQL table.

## Validation Rules
- `url` must be a valid HTTP/HTTPS URL.
- `text` chunk size must not exceed Cohere's token limit (approx 512 tokens).
- `vector` must have exactly 1024 dimensions.
