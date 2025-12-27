# Website

This website is built using [Docusaurus](https://docusaurus.io/), a modern static website generator.

## Installation

```bash
yarn
```

## Local Development

```bash
yarn start
```

This command starts a local development server and opens up a browser window. Most changes are reflected live without having to restart the server.

## Build

```bash
yarn build
```

This command generates static content into the `build` directory and can be served using any static contents hosting service.

## Deployment

Using SSH:

```bash
USE_SSH=true yarn deploy
```

Not using SSH:

```bash
GIT_USER=<Your GitHub username> yarn deploy
```

If you are using GitHub pages for hosting, this command is a convenient way to build the website and push to the `gh-pages` branch.

## RAG Agent Integration

This project includes a RAG (Retrieval-Augmented Generation) agent that interacts with the documentation.

### Prerequisites

- Python 3.11+
- Node.js 18+
- Backend dependencies: `uv pip install -r backend/requirements.txt` (or manually as below)

### Running the Backend

1. Ensure the virtual environment is set up and dependencies are installed:
   ```bash
   uv pip install fastapi uvicorn beautifulsoup4 click cohere httpx openai openai-agents python-dotenv qdrant-client
   ```
2. Start the FastAPI server from the project root:
   ```bash
   ./.venv/Scripts/python -m uvicorn backend.api:app --reload --port 8000
   ```
   (Adjust python path if using a different venv)

### Running the Frontend

1. Install frontend dependencies:
   ```bash
   npm install
   ```
2. Start the development server:
   ```bash
   npm start
   ```
3. Open `http://localhost:3000`. The RAG Agent chat widget should be visible in the bottom right corner.

### Configuration

- Create a `.env` file in the root directory with necessary API keys (OpenAI, OpenRouter, etc.).
# Ai-chatbot-book
