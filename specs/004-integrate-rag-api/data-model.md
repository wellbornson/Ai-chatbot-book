# Data Model

## Entities

### QueryRequest
Represents a user's question sent to the agent.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| query | string | Yes | The text of the user's question. |
| thread_id | string | No | Optional ID to maintain conversation state. |

### QueryResponse
Represents the agent's answer.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| response | string | Yes | The markdown-formatted text response from the agent. |
| thread_id | string | Yes | The ID of the conversation thread (returned for client state). |
| status | string | Yes | "success" or "error". |

## Validation Rules
- `query`: Must not be empty or whitespace only. Max length 1000 chars.
