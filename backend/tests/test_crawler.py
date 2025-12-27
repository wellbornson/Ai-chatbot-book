import pytest
from crawler import parse_sitemap, extract_text

def test_parse_sitemap():
    sitemap_xml = """
    <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
        <url><loc>https://example.com/page1</loc></url>
        <url><loc>https://example.com/page2</loc></url>
    </urlset>
    """
    urls = parse_sitemap(sitemap_xml)
    assert urls == ["https://example.com/page1", "https://example.com/page2"]

def test_extract_text(sample_html):
    data = extract_text(sample_html)
    assert data["title"] == "Main Heading"
    assert "This is some test content for chunking." in data["text"]
    assert "Another paragraph" in data["text"]
    assert "Test Page" not in data["text"] # should only get article content
