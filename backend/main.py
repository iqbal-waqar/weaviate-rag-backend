from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.rag_routes import router as rag_router

load_dotenv()

app = FastAPI(title="PDF RAG System with Weaviate Cloud")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(rag_router)

@app.get("/")
def health_check():
    return {"status": "healthy", "message": "PDF RAG System is running"}

@app.get("/health")
def health():
    return {"status": "ok"}
