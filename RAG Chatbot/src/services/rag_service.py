from .qdrant_service import QdrantVectorDBService
from .cohere_service import CohereEmbeddingService
from cohere import Client
from ..core.config import get_settings

settings = get_settings()

class RAGService:
    """
    Service for handling the RAG pipeline: embedding query, searching for context,
    and generating an answer with a language model.
    """

    def __init__(self):
        self.qdrant_service = QdrantVectorDBService()
        self.embedding_service = CohereEmbeddingService()
        self.cohere_client = Client(settings.COHERE_API_KEY)
        self.model = "command-r"

    def generate_answer(self, query: str) -> str:
        """
        Generates an answer to a query using the RAG pipeline.
        """
        print(f"Generating answer for query: '{query}'")

        # 1. Embed the user's query
        self.embedding_service.input_type = "search_query"
        query_embedding = self.embedding_service.embed_texts([query])
        
        if not query_embedding:
            print("Failed to embed query.")
            return "Sorry, there was an error processing your question."

        # 2. Search for relevant context in Qdrant
        search_results = self.qdrant_service.search_vectors(query_embedding[0], limit=3)
        
        if not search_results:
            print("No relevant context found in the book.")
            return "This information is not available in the book."

        # 3. Build the prompt with the retrieved context
        context = "\n".join([result["payload"]["text"] for result in search_results])
        
        prompt = f"""
        You are a helpful assistant for the book "Physical AI & Humanoid Robotics".
        Answer the user's question based *only* on the following context from the book.
        Do not use any external knowledge. If the answer is not found in the context,
        say "This information is not available in the book.".
        Keep the answer concise and clear (3-5 lines).

        Context from the book:
        ---
        {context}
        ---

        User's question: {query}        
        Answer:
        """

        # 4. Generate an answer with Cohere's Chat model
        try:
            print("Generating answer with Cohere...")
            response = self.cohere_client.chat(
                model=self.model,
                message=prompt,
                # The connectors param can be used to ground the model on specific documents,
                # but here we are manually providing the context in the prompt.
            )
            answer = response.text
            print(f"Generated answer: {answer}")
            return answer
        except Exception as e:
            print(f"Error generating answer with Cohere Chat: {e}")
            return "Sorry, there was an error generating the answer."

# Example Usage
if __name__ == "__main__":
    # from dotenv import load_dotenv
    # load_dotenv()
    
    rag_service = RAGService()
    test_query = "What is FastAPI?" # Assuming content about FastAPI is in the ingested data
    answer = rag_service.generate_answer(test_query)
    print("\n---", "Final Answer", "---")
    print(answer)
