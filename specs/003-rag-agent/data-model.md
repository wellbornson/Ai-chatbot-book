# Data Model: RAG Agent

## Entities

### Agent Configuration
- **Model**: `gpt-4o` (or similar, capable of tool use)
- **Instructions**: System prompt defining the agent's persona and strict adherence to retrieval tools.
- **Tools**: List of enabled tools (`search_knowledge_base`).

### Tool: `search_knowledge_base`
- **Name**: `search_knowledge_base`
- **Description**: "Searches the internal knowledge base (books/docs) for relevant information. Use this for ANY question about [Topic]."
- **Parameters**:
  - `query` (string, required): The search query optimized for similarity search.

### Conversation State
- Managed by OpenAI Threads.
- **Thread ID**: Unique identifier for the conversation session.
