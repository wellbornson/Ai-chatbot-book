# CLI Contract: Agent Interaction

## Command: `ask`

Interact with the agent via command line.

### Usage
```bash
uv run agent.py ask "How do I deploy?"
```

### Arguments
- `question` (string): The user's prompt.

### Options
- `--new`: Start a new conversation thread (clears history).
- `--thread-id`: Resume a specific conversation thread.

### Output
Streaming or final text response from the agent.
Debug logs showing tool calls (if enabled).
