from typing import List

class TextSplitter:
    """
    A utility class to split large text content into smaller, manageable chunks.
    Simple implementation for now, can be expanded with more sophisticated methods.
    """

    def __init__(self, chunk_size: int = 500, chunk_overlap: int = 50):
        """
        Initializes the TextSplitter.

        Args:
            chunk_size (int): The maximum size of each text chunk.
            chunk_overlap (int): The number of characters to overlap between consecutive chunks.
        """
        if chunk_overlap >= chunk_size:
            raise ValueError("Chunk overlap must be less than chunk size.")
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def split_text(self, text: str) -> List[str]:
        """
        Splits a given text into chunks.
        """
        if not text:
            return []

        chunks = []
        start = 0
        while start < len(text):
            end = start + self.chunk_size
            chunk = text[start:end]
            chunks.append(chunk)
            start += self.chunk_size - self.chunk_overlap
            if start >= len(text) - self.chunk_overlap: # Avoid endless loop if overlap is too large for remaining text
                break
        return chunks

# Example Usage
if __name__ == "__main__":
    long_text = "This is a very long piece of text that needs to be split into smaller chunks. Each chunk should be of a certain size, and there should be some overlap between consecutive chunks to ensure context is maintained across the splits. This is crucial for retrieval-augmented generation systems where the context size of the language model is limited."
    
    splitter = TextSplitter(chunk_size=100, chunk_overlap=20)
    chunks = splitter.split_text(long_text)
    
    print(f"Original text length: {len(long_text)}")
    print(f"Number of chunks: {len(chunks)}")
    for i, chunk in enumerate(chunks):
        print(f"--- Chunk {i+1} (length: {len(chunk)}) ---")
        print(chunk)
