import pytest
from unittest.mock import MagicMock, patch, AsyncMock
import sys
import os
import asyncio

# Ensure backend can be imported
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from agent import rag_agent, search_knowledge_base_logic

def test_agent_configuration():
    assert rag_agent.name == "RAG Agent"
    assert rag_agent.model == "gpt-4o"
    assert len(rag_agent.tools) == 1
    assert rag_agent.tools[0].name == "search_knowledge_base"

def test_search_tool_logic():
    with patch("agent.perform_search") as mock_search:
        mock_result = MagicMock()
        mock_result.title = "Test Doc"
        mock_result.url = "http://test.com"
        mock_result.text = "Content..."
        mock_search.return_value = [mock_result]
        
        output = search_knowledge_base_logic("query")
        
        assert "Test Doc" in output
        assert "http://test.com" in output
        mock_search.assert_called_with("query", limit=3)

@pytest.mark.asyncio
async def test_runner_run_flow():
    with patch("agent.Runner.run", new_callable=AsyncMock) as mock_run:
        mock_result = MagicMock()
        mock_result.final_output = "Hello from Agent"
        mock_run.return_value = mock_result
        
        from agents import Runner
        res = await Runner.run(rag_agent, "Hi")
        assert res.final_output == "Hello from Agent"