import logging
import cohere
from storage import get_config

def chunk_text(text, chunk_size=512, overlap=50):
    """
    Split text into chunks by word count.
    Note: Real production might use token-based chunking.
    """
    words = text.split()
    chunks = []
    
    if not words:
        return chunks
        
    for i in range(0, len(words), chunk_size - overlap):
        chunk = " ".join(words[i : i + chunk_size])
        chunks.append(chunk)
        if i + chunk_size >= len(words):
            break
            
    return chunks

class EmbeddingGenerator:
    def __init__(self):
        config = get_config()
        self.client = cohere.ClientV2(config.COHERE_API_KEY)
        self.model = "embed-english-v3.0"

    def generate_embeddings(self, texts):
        """Generate embeddings for a list of text chunks."""
        try:
            response = self.client.embed(
                texts=texts,
                model=self.model,
                input_type="search_document",
                embedding_types=["float"]
            )
            return response.embeddings.float
        except Exception as e:
            logging.error(f"Error generating embeddings: {e}")
            raise

    def generate_query_embedding(self, query):
        """Generate embedding for a single search query."""
        try:
            response = self.client.embed(
                texts=[query],
                model=self.model,
                input_type="search_query",
                embedding_types=["float"]
            )
            return response.embeddings.float[0]
        except Exception as e:
            logging.error(f"Error generating query embedding: {e}")
            raise
