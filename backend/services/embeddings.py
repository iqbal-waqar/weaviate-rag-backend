class EmbeddingsService:
    """
    Embeddings service - using Weaviate's built-in text2vec module
    instead of local sentence-transformers to reduce deployment size
    """
    
    def __init__(self, model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
        self.model_name = model_name
    
    def get_embeddings(self):
        # Return None to use Weaviate's built-in vectorization
        # Weaviate Cloud handles embeddings with text2vec modules
        return None
