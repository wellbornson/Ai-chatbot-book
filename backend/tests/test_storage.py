import pytest
from unittest.mock import MagicMock
from storage import VectorStore

def test_search_results_parsing(mock_qdrant):
    # Mock search result from qdrant
    mock_res = [
        MagicMock(payload={"title": "Page 1", "url": "url1", "text": "text1"}, score=0.9),
        MagicMock(payload={"title": "Page 2", "url": "url2", "text": "text2"}, score=0.8)
    ]
    mock_qdrant.search.return_value = mock_res
    
    store = VectorStore()
    store.client = mock_qdrant # Inject mock
    
    results = store.search([0.1]*1024)
    
    assert len(results) == 2
    assert results[0]["title"] == "Page 1"
    assert results[1]["score"] == 0.8
