import pytest
from processor import chunk_text

def test_chunk_text():
    text = "Word " * 100 # 100 words
    # Suppose we want small chunks for testing
    chunks = chunk_text(text, chunk_size=20, overlap=5)
    
    assert len(chunks) > 1
    assert all(len(c.split()) <= 20 for c in chunks)
    # Check overlap (last 5 words of chunk 1 should be start of chunk 2)
    words1 = chunks[0].split()
    words2 = chunks[1].split()
    assert words1[-5:] == words2[:5]
