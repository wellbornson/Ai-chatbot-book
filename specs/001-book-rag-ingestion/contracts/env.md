# Environment Variables Contract

The system requires the following environment variables to be set in a `.env` file or the shell environment.

| Variable | Required | Description |
|----------|----------|-------------|
| `COHERE_API_KEY` | Yes | API key for generating embeddings. |
| `QDRANT_URL` | Yes | The URL of the Qdrant Cloud instance. |
| `QDRANT_API_KEY` | Yes | API key for Qdrant Cloud. |
| `LOG_LEVEL` | No | Logging verbosity (INFO, DEBUG, ERROR). Default: INFO. |
