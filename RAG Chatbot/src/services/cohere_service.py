from cohere import Client
from typing import List
from ..core.config import get_settings

settings = get_settings()

class CohereEmbeddingService:
    """
    Service for generating embeddings using the Cohere API.
    """

    def __init__(self):
        self.co = Client(settings.COHERE_API_KEY)
        self.model = "embed-english-v3.0" # or "embed-english-light-v3.0", "embed-multilingual-v3.0"
        self.input_type = "search_document" # or "search_query"

    def embed_texts(self, texts: List[str]) -> List[List[float]]:
        """
        Generates embeddings for a list of texts.
        """
        if not texts:
            return []
        print(f"Generating embeddings for {len(texts)} texts using Cohere model '{self.model}'...")
        try:
            response = self.co.embed(
                texts=texts,
                model=self.model,
                input_type=self.input_type
            ).embeddings
            print(f"Generated {len(response)} embeddings, each with dimension {len(response[0])}.")
            return response
        except Exception as e:
            print(f"Error generating embeddings with Cohere: {e}")
            return []

# Example Usage (requires COHERE_API_KEY to be set in .env)
if __name__ == "__main__":
    # from dotenv import load_dotenv
    # load_dotenv()

    embedding_service = CohereEmbeddingService()
    
    sample_texts = [
        "What is the capital of France?",
        "How hot is the sun?",
        "What is the best way to learn programming?"
    ]
    
    embeddings = embedding_service.embed_texts(sample_texts)
    
    if embeddings:
        print("\nEmbeddings generated successfully. First embedding snippet:")
        print(embeddings[0][:5]) # Print first 5 dimensions of the first embedding
    else:
        print("Failed to generate embeddings.")
