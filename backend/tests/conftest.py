import pytest
from unittest.mock import MagicMock

@pytest.fixture
def mock_cohere():
    return MagicMock()

@pytest.fixture
def mock_qdrant():
    return MagicMock()

@pytest.fixture
def sample_html():
    return """
    <html>
        <head><title>Test Page</title></head>
        <body>
            <article class="theme-doc-markdown">
                <h1>Main Heading</h1>
                <p>This is some test content for chunking.</p>
                <p>Another paragraph to ensure we have enough text.</p>
            </article>
        </body>
    </html>
    """
