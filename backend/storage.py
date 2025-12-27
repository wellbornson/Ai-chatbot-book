import os
import logging
from dotenv import load_dotenv
from qdrant_client import QdrantClient
from qdrant_client.http import models

# Load environment variables from .env file
load_dotenv(override=True)

class Config:
    COHERE_API_KEY = os.getenv("COHERE_API_KEY")
    QDRANT_URL = os.getenv("QDRANT_URL")
    QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

    @classmethod
    def validate(cls):
        missing = []
        if not cls.COHERE_API_KEY: missing.append("COHERE_API_KEY")
        if not cls.QDRANT_URL: missing.append("QDRANT_URL")
        if not cls.QDRANT_API_KEY: missing.append("QDRANT_API_KEY")
        
        if missing:
            raise ValueError(f"Missing required environment variables: {', '.join(missing)}")

def get_config():
    config = Config()
    return config

class VectorStore:
    def __init__(self, collection_name="documentation"):
        config = get_config()
        self.collection_name = collection_name
        self.client = QdrantClient(
            url=config.QDRANT_URL,
            api_key=config.QDRANT_API_KEY,
        )

    def ensure_collection(self, vector_size=1024):
        """Create collection if it doesn't exist."""
        collections = self.client.get_collections().collections
        exists = any(c.name == self.collection_name for c in collections)
        
        if not exists:
            logging.info(f"Creating collection: {self.collection_name}")
            self.client.create_collection(
                collection_name=self.collection_name,
                vectors_config=models.VectorParams(
                    size=vector_size,
                    distance=models.Distance.COSINE
                ),
            )

    def upsert_chunks(self, chunks_with_embeddings):
        """
        chunks_with_embeddings: List of dicts with:
        id, vector, metadata (text, url, title)
        """
        points = [
            models.PointStruct(
                id=item["id"],
                vector=item["vector"],
                payload=item["metadata"]
            )
            for item in chunks_with_embeddings
        ]
        
        self.client.upsert(
            collection_name=self.collection_name,
            points=points
        )

    def search(self, query_vector, limit=5):
        """Perform similarity search."""
        hits = self.client.query_points(
            collection_name=self.collection_name,
            query=query_vector,
            limit=limit
        ).points
        
        results = []
        for hit in hits:
            results.append({
                "score": hit.score,
                "title": hit.payload.get("title"),
                "url": hit.payload.get("url"),
                "text": hit.payload.get("text")
            })
        return results
