from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api import chat as chat_api
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = FastAPI(
    title="Website RAG Chatbot API",
    version="1.0.0",
    description="API for the book website's RAG chatbot."
)

# Set up CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Include the chat API router
app.include_router(chat_api.router, prefix="/api/v1", tags=["Chat"])

@app.get("/", tags=["Health Check"])
async def root():
    """
    Root endpoint for health checks.
    """
    return {"status": "ok"}
