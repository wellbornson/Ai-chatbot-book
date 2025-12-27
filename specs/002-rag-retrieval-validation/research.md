# Research: Retrieval & Pipeline Validation

**Status**: Complete
**Date**: 2025-12-24

## Decisions & Rationale

### 1. Script Location
- **Decision**: Place `retrieve.py` in `backend/` directory.
- **Rationale**: The project uses `uv` for dependency management within the `backend/` directory. Placing the script there allows it to easily import from `storage.py` and usage of the installed venv. Placing it in the root would require complex python path setups or a separate venv.
- **Alternatives Considered**: Root directory (rejected due to dependency management friction).

### 2. Qdrant API Method
- **Decision**: Use `client.query_points()` instead of `client.search()`.
- **Rationale**: Investigation during the previous feature (Feature 001) revealed that the installed version of `qdrant-client` does not support the `search` method on the client object directly, or usage patterns have shifted. `query_points` is the robust, supported method for the current version.
- **Alternatives Considered**: Downgrading `qdrant-client` (rejected to maintain currency).

### 3. Metadata Validation Strategy
- **Decision**: Perform an HTTP HEAD/GET request to the source URL found in metadata.
- **Rationale**: Verifies not just that the URL exists in the DB, but that it is reachable on the internet, satisfying the "Verify Metadata Integrity" user story.
- **Alternatives Considered**: String validation only (rejected as it doesn't prove reachability).

## Unknowns Resolved

- **Qdrant Connection**: Validated in Feature 001.
- **Embedding Model**: Cohere `embed-english-v3.0` (validated).
