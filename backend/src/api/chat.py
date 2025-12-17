from fastapi import APIRouter, Depends
from ..models.chat import UserQuery, GeneratedResponse
from ..services.rag_service import RAGService

router = APIRouter()

@router.post("/chat", response_model=GeneratedResponse)
async def get_chatbot_response(
    query: UserQuery, 
    rag_service: RAGService = Depends(RAGService)
):
    """
    Handles a user's query and returns a generated response from the RAG pipeline.
    """
    answer = rag_service.generate_answer(query.query)
    return GeneratedResponse(response=answer)
