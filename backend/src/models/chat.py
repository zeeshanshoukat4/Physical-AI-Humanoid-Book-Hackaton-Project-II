from pydantic import BaseModel, Field

class UserQuery(BaseModel):
    """
    Pydantic model for the user query request body.
    """
    query: str = Field(..., min_length=1, max_length=500, description="The user's question.")

class GeneratedResponse(BaseModel):
    """
    Pydantic model for the chatbot's response.
    """
    response: str = Field(..., description="The generated answer or a standard message.")
