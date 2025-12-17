import time
from src.services.data_loader import DataLoader
from src.core.text_splitter import TextSplitter
from src.services.cohere_service import CohereEmbeddingService
from src.services.qdrant_service import QdrantVectorDBService
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def main():
    """
    Main function to run the data ingestion pipeline.
    """
    print("Starting data ingestion pipeline...")
    
    # 1. Initialize services
    data_loader = DataLoader()
    text_splitter = TextSplitter(chunk_size=250, chunk_overlap=30)
    embedding_service = CohereEmbeddingService()
    qdrant_service = QdrantVectorDBService()

    # 2. Recreate Qdrant collection (optional, use with caution)
    qdrant_service.recreate_collection()

    # 3. Fetch sitemap URLs
    sitemap_urls = data_loader.fetch_sitemap_urls()
    if not sitemap_urls:
        print("No URLs found. Exiting.")
        return

    # 4. Process each URL
    all_chunks = []
    all_payloads = []
    for url in sitemap_urls:
        content_data = data_loader.fetch_url_content(url)
        if content_data and "content" in content_data:
            # Simple text extraction for now, can be improved with BeautifulSoup
            raw_text = content_data["content"]
            
            # Here you might want to use BeautifulSoup to extract meaningful text
            # from HTML. For now, we'll use the raw text.
            
            chunks = text_splitter.split_text(raw_text)
            payloads = [{"source_url": url, "text": chunk} for chunk in chunks]
            
            all_chunks.extend(chunks)
            all_payloads.extend(payloads)
        time.sleep(0.5) # Be nice to the server

    if not all_chunks:
        print("No content to process. Exiting.")
        return

    # 5. Process in batches to avoid rate limiting
    batch_size = 90  # Cohere's API has a limit, typically 96 for embed v3
    for i in range(0, len(all_chunks), batch_size):
        batch_chunks = all_chunks[i:i + batch_size]
        batch_payloads = all_payloads[i:i + batch_size]
        
        print(f"\n--- Processing batch {i//batch_size + 1}/{(len(all_chunks) + batch_size - 1)//batch_size} ---")

        # 5a. Generate embeddings for the batch
        embeddings = embedding_service.embed_texts(batch_chunks)

        if not embeddings:
            print(f"Failed to generate embeddings for batch {i//batch_size + 1}. Skipping.")
            continue

        # 5b. Upsert vectors and payloads to Qdrant
        # Generate unique IDs for this batch
        batch_ids = list(range(i, i + len(batch_chunks)))
        qdrant_service.upsert_vectors(embeddings, batch_payloads, ids=batch_ids)
        
        print(f"Batch {i//batch_size + 1} processed. Waiting 5 seconds...")
        time.sleep(5)

    print("Data ingestion pipeline completed successfully.")


if __name__ == "__main__":
    main()
