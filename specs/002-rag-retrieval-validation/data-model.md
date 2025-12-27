# Data Model: Retrieval Validation

## Entities

### RetrievalResult

Represents a single chunk of text retrieved from the vector store.

| Field | Type | Description |
|-------|------|-------------|
| `text` | `str` | The content text chunk. |
| `score` | `float` | Cosine similarity score (0.0 - 1.0). |
| `url` | `str` | Source URL of the document. |
| `title` | `str` | Title of the source document. |
| `id` | `str` | UUID of the vector point. |

### ValidationReport

Represents the outcome of a validation run.

| Field | Type | Description |
|-------|------|-------------|
| `query` | `str` | The search query used. |
| `results_found` | `int` | Number of results retrieved. |
| `top_score` | `float` | Highest similarity score found. |
| `valid_urls` | `int` | Count of URLs that returned 200 OK. |
| `status` | `enum` | PASS/FAIL based on criteria. |
