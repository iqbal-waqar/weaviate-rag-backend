import os
import weaviate
from langchain_community.vectorstores import Weaviate
from services.embeddings import EmbeddingsService
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


class WeaviateService:
    INDEX_NAME = "PakistanLawPDFRAG"
    
    def __init__(self):
        self.embeddings_service = EmbeddingsService()
    
    def get_client(self):
        url = os.getenv("WEAVIATE_URL")
        api_key = os.getenv("WEAVIATE_API_KEY", None)
        
        if not url:
            raise ValueError("WEAVIATE_URL environment variable is not set. Please check your .env file.")
        
        if api_key:
            client = weaviate.Client(
                url=url,
                auth_client_secret=weaviate.AuthApiKey(api_key),
                timeout_config=(5, 60),  
                startup_period=10  
            )
        else:
            client = weaviate.Client(
                url=url,
                timeout_config=(5, 60),
                startup_period=10
            )

        if not client.is_ready():
            raise Exception("Weaviate cluster not ready or cannot connect")
        return client

    def load_pdf_into_weaviate(self, pdf_path: str = "data/Pakistan-Law.pdf"):
        client = self.get_client()
        embeddings = self.embeddings_service.get_embeddings()

        loader = PyPDFLoader(pdf_path)
        documents = loader.load()

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1200,
            chunk_overlap=150
        )
        chunks = splitter.split_documents(documents)

        Weaviate.from_documents(
            chunks,
            embeddings,
            client=client,
            index_name=self.INDEX_NAME
        )

    def load_pdf_once(self, pdf_path: str = "data/Pakistan-Law.pdf"):
        client = self.get_client()

        schema = client.schema.get()
        existing_classes = [cls["class"] for cls in schema.get("classes", [])]

        if self.INDEX_NAME not in existing_classes:
            self.load_pdf_into_weaviate(pdf_path)

    def get_vectorstore(self):

        client = self.get_client()
        embeddings = self.embeddings_service.get_embeddings()
        return Weaviate(
            client=client,
            index_name=self.INDEX_NAME,
            text_key="text",
            embedding=embeddings,
            by_text=False  
        )
