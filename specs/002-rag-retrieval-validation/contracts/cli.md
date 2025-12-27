# CLI Contract: Retrieve Script

**Command**: `uv run backend/retrieve.py`

## Arguments

| Argument | Type | Required | Description |
|----------|------|----------|-------------|
| `query` | `str` | Yes | The natural language search query. |
| `--limit` | `int` | No | Number of results to return (default: 5). |
| `--validate/--no-validate` | `bool` | No | Whether to check URL reachability (default: True). |

## Output (Stdout)

### Success (JSON format for machine readability optional, human-readable default)

```text
Validation Report:
------------------
Query: "how to deploy"
Status: PASS
Top Score: 0.89
Valid URLs: 5/5

Results:
1. [0.89] Deploy your site - https://book-chatbot-aa1u.vercel.app/deploy
   "Snippet of text..."
...
```

### Error (Stderr)

```text
Error: Failed to connect to Qdrant.
Details: [Exception message]
```
