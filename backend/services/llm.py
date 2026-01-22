from langchain_groq import ChatGroq
import os


class LLMService:
    
    def __init__(self, model_name: str = "llama-3.3-70b-versatile", temperature: float = 0):
        self.model_name = model_name
        self.temperature = temperature
    
    def get_llm(self):
        return ChatGroq(
            groq_api_key=os.getenv("GROQ_API_KEY"),
            model_name=self.model_name,
            temperature=self.temperature  
        )
