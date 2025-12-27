import pytest
import httpx
from unittest.mock import MagicMock, AsyncMock, patch
from retrieve import RetrievalResult, ValidationReport, perform_search, format_results, validate_urls

@pytest.fixture
def mock_qdrant():
    with patch("retrieve.VectorStore") as mock:
        yield mock

@pytest.fixture
def mock_embedder():
    with patch("retrieve.EmbeddingGenerator") as mock:
        yield mock

def test_retrieval_result_creation():
    result = RetrievalResult(
        text="Test text",
        score=0.95,
        url="https://example.com",
        title="Test Title",
        id="123"
    )
    assert result.text == "Test text"
    assert result.score == 0.95

def test_perform_search(mock_qdrant, mock_embedder):
    # Setup
    mock_embedder.return_value.generate_query_embedding.return_value = [0.1, 0.2]
    mock_qdrant.return_value.search.return_value = [
        {"score": 0.9, "title": "T1", "url": "U1", "text": "Text1"}
    ]
    
    # Execute
    results = perform_search("test query", limit=1)
    
    # Verify
    assert len(results) == 1
    assert results[0].title == "T1"
    mock_embedder.return_value.generate_query_embedding.assert_called_with("test query")
    mock_qdrant.return_value.search.assert_called_once()

def test_format_results():
    results = [
        RetrievalResult(text="Snippet...", score=0.88, url="http://u", title="Title", id="1")
    ]
    report = ValidationReport(query="q", results_found=1, top_score=0.88, valid_urls=1, status="PASS")
    
    formatted = format_results(results, report)
    assert "Query: \"q\"" in formatted
    assert "Status: PASS" in formatted
    assert "Title" in formatted

@pytest.mark.asyncio
async def test_validate_urls():
    results = [
        RetrievalResult(text="t1", score=0.9, url="https://ok.com", title="ok"),
        RetrievalResult(text="t2", score=0.8, url="https://fail.com", title="fail"),
    ]
    
    # Mock httpx response
    async def mock_head(url, **kwargs):
        resp = MagicMock(spec=httpx.Response)
        resp.status_code = 200 if "ok.com" in url else 404
        if "fail.com" in url:
            resp.raise_for_status.side_effect = Exception("404")
        return resp

    with patch("httpx.AsyncClient.head", side_effect=mock_head):
        valid_count = await validate_urls(results)
        assert valid_count == 1
