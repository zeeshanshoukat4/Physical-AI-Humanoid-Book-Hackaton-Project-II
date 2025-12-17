from qdrant_client import QdrantClient, models
from qdrant_client.http.models import Distance, VectorParams
from typing import List, Dict, Optional
from ..core.config import get_settings

settings = get_settings()

class QdrantVectorDBService:
    """
    Service for interacting with Qdrant Cloud as a vector database.
    """

    def __init__(self, collection_name: str = "book_content"):
        self.client = QdrantClient(
            url=settings.QDRANT_CLUSTER_URL,
            api_key=settings.QDRANT_API_KEY,
        )
        self.collection_name = collection_name
        self.vector_size = 1024  # Cohere embeddings typically are 1024 dimensions

    def recreate_collection(self):
        """
        Deletes and recreates the Qdrant collection. Use with caution.
        """
        print(f"Recreating collection '{self.collection_name}'...")
        self.client.recreate_collection(
            collection_name=self.collection_name,
            vectors_config=VectorParams(size=self.vector_size, distance=Distance.COSINE),
        )
        print(f"Collection '{self.collection_name}' recreated.")

    def upsert_vectors(self, vectors: List[List[float]], payloads: List[Dict], ids: Optional[List[int]] = None):
        """
        Upserts vectors and their associated payloads into the Qdrant collection.
        """
        if not vectors or not payloads:
            print("No vectors or payloads to upsert.")
            return

        print(f"Upserting {len(vectors)} vectors into collection '{self.collection_name}'...")
        self.client.upsert(
            collection_name=self.collection_name,
            wait=True,
            points=models.Batch(
                ids=ids,
                vectors=vectors,
                payloads=payloads
            ),
        )
        print(f"Upserted {len(vectors)} vectors successfully.")

    def search_vectors(self, query_vector: List[float], limit: int = 5) -> List[Dict]:
        """
        Searches the Qdrant collection for vectors similar to the query vector.
        """
        print(f"Searching collection '{self.collection_name}' for similar vectors...")
        search_result = self.client.search(
            collection_name=self.collection_name,
            query_vector=query_vector,
            limit=limit,
            with_payload=True
        )
        results = []
        for scored_point in search_result:
            results.append({
                "id": scored_point.id,
                "score": scored_point.score,
                "payload": scored_point.payload
            })
        print(f"Found {len(results)} search results.")
        return results

# Example Usage (requires Qdrant to be running and API key/URL set)
if __name__ == "__main__":
    # Ensure .env is configured with QDRANT_API_KEY and QDRANT_CLUSTER_URL
    # from dotenv import load_dotenv
    # load_dotenv()

    service = QdrantVectorDBService()
    service.recreate_collection()

    # Dummy data
    dummy_vectors = [[0.1, 0.2, 0.3, ..., 1.0] for _ in range(3)] # Should be 1024 dim
    # Create 1024-dim dummy vectors
    dummy_vectors = [[float(i) / 1024 for i in range(1024)] for _ in range(3)]

    dummy_payloads = [
        {"text": "Python is a programming language.", "source": "page1.md"},
        {"text": "FastAPI is a modern, fast (high-performance) web framework for building APIs with Python.", "source": "page2.md"},
        {"text": "Qdrant is a vector similarity search engine.", "source": "page3.md"},
    ]
    
    # service.upsert_vectors(dummy_vectors, dummy_payloads)

    # Example search (requires a dummy query vector)
    # query_vector = [0.11, 0.21, 0.31, ..., 1.01] # Should be 1024 dim
    query_vector = [float(i) / 1024 + 0.01 for i in range(1024)]
    # search_results = service.search_vectors(query_vector)
    # print("Search results:", search_results)
