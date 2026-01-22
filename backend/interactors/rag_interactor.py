from services.weaviate import WeaviateService
from services.llm import LLMService
from services.prompts import RAG_PROMPT, GREETING_RESPONSES
import random


class RAGInteractor:

    GREETINGS = [
        'hello', 'hi', 'hey', 'greetings', 'good morning', 'good afternoon', 
        'good evening', 'howdy', 'what\'s up', 'whats up', 'sup', 'yo',
        'how are you', 'how do you do', 'nice to meet you', 'salaam', 'salam',
        'assalam', 'assalamu alaikum'
    ]
    
    def __init__(self):
        self.weaviate_service = WeaviateService()
        self.llm_service = LLMService()
    
    def is_greeting(self, question: str) -> bool:
        
        question_lower = question.lower().strip()
        if len(question_lower.split()) <= 5:
            for greeting in self.GREETINGS:
                if greeting in question_lower:
                    return True
        return False
    
    def get_greeting_response(self) -> str:

        return random.choice(GREETING_RESPONSES)
    
    def answer_question(self, question: str) -> str:

        if self.is_greeting(question):
            return self.get_greeting_response()
        
        vectorstore = self.weaviate_service.get_vectorstore()
        llm = self.llm_service.get_llm()

        docs = vectorstore.similarity_search(question, k=10)
        context = "\n\n".join([doc.page_content for doc in docs])

        chain = RAG_PROMPT | llm
        
        response = chain.invoke({
            "context": context,
            "question": question
        })

        return response.content.strip()
