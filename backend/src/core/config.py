from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    """
    Application settings loaded from environment variables.
    """
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    # Qdrant settings
    QDRANT_API_KEY: str
    QDRANT_CLUSTER_URL: str

    # Cohere settings
    COHERE_API_KEY: str

    # Neon PostgreSQL settings (if needed, though not directly used in RAG pipeline initially)
    NEON_DATABASE_URL: str
    
    # Sitemap URL for content ingestion
    SITEMAP_URL: str = "https://physical-ai-humanoid-book-hackaton-zeta.vercel.app/sitemap.xml"


@lru_cache()
def get_settings():
    """
    Get cached settings instance.
    """
    return Settings()

