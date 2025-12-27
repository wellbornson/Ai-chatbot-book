import httpx
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import logging

def parse_sitemap(xml_content):
    """Extract URLs from a sitemap XML."""
    urls = []
    try:
        root = ET.fromstring(xml_content)
        # Handle namespaces
        ns = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
        for url in root.findall('ns:url', ns):
            loc = url.find('ns:loc', ns)
            if loc is not None and loc.text:
                urls.append(loc.text)
    except Exception as e:
        logging.error(f"Error parsing sitemap: {e}")
    return urls

def extract_text(html_content):
    """Extract main content and title from Docusaurus HTML."""
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Try to find the main content article
    article = soup.find('article')
    if not article:
        # Fallback to a common Docusaurus class
        article = soup.select_one('.theme-doc-markdown')
    
    title = ""
    if article:
        h1 = article.find('h1')
        if h1:
            title = h1.get_text(strip=True)
        
        # Remove unwanted elements before extracting text
        for tag in article.find_all(['nav', 'footer', 'script', 'style']):
            tag.decompose()
            
        text = article.get_text(separator=' ', strip=True)
    else:
        # Final fallback: just get all body text
        text = soup.body.get_text(separator=' ', strip=True) if soup.body else ""

    return {
        "title": title or "Untitled Page",
        "text": text
    }

async def fetch_url(url):
    """Fetch content of a URL."""
    async with httpx.AsyncClient() as client:
        response = await client.get(url, follow_redirects=True)
        response.raise_for_status()
        return response.text
