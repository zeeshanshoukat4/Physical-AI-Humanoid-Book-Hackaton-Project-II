from fastapi.testclient import TestClient
from src.main import app
from src.services.rag_service import RAGService
import pytest

client = TestClient(app)

@pytest.fixture
def mock_rag_service(monkeypatch):
    """
    Mocks the RAGService to avoid actual API calls to Cohere and Qdrant.
    """
    def mock_generate_answer(self, query: str) -> str:
        if "error" in query:
            return "Sorry, there was an error processing your question."
        if "not found" in query:
            return "This information is not available in the book."
        return f"This is a mocked answer for the query: '{query}'"
        
    monkeypatch.setattr(RAGService, "generate_answer", mock_generate_answer)


def test_get_chatbot_response_success(mock_rag_service):
    """
    Test the /api/v1/chat endpoint for a successful response.
    """
    response = client.post("/api/v1/chat", json={"query": "What is a test?"})
    assert response.status_code == 200
    json_response = response.json()
    assert "response" in json_response
    assert "This is a mocked answer" in json_response["response"]
    assert "What is a test?" in json_response["response"]

def test_get_chatbot_response_not_found(mock_rag_service):
    """
    Test the /api/v1/chat endpoint for a 'not found' response.
    """
    response = client.post("/api/v1/chat", json={"query": "not found query"})
    assert response.status_code == 200
    json_response = response.json()
    assert json_response["response"] == "This information is not available in the book."

def test_get_chatbot_response_invalid_query_short():
    """
    Test the API with a query that is too short (should fail validation).
    """
    response = client.post("/api/v1/chat", json={"query": ""})
    # FastAPI returns 422 for validation errors
    assert response.status_code == 422 

def test_get_chatbot_response_invalid_query_long():
    """
    Test the API with a query that is too long (should fail validation).
    """
    long_query = "a" * 501
    response = client.post("/api/v1/chat", json={"query": long_query})
    assert response.status_code == 422
