from langchain_community.embeddings import FastEmbedEmbeddings


class EmbeddingsService:
    """
    Using FastEmbed - Free, Local, and Lightweight (No heavy Torch dependency)
    Uses the same model architecture as sentence-transformers but optimized.
    """
    
    def __init__(self, model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
        self.model_name = model_name
    
    def get_embeddings(self):
        return FastEmbedEmbeddings(
            model_name=self.model_name
        )
