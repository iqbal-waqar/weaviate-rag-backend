from langchain_community.embeddings import HuggingFaceEmbeddings


class EmbeddingsService:

    def __init__(self, model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
        self.model_name = model_name
    
    def get_embeddings(self):
        return HuggingFaceEmbeddings(
            model_name=self.model_name
        )
