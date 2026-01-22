from fastapi import APIRouter
from schemas.rag_schema import QuestionRequest, AnswerResponse
from interactors.rag_interactor import RAGInteractor

router = APIRouter(prefix="/rag", tags=["RAG"])

rag_interactor = RAGInteractor()


@router.post("/ask", response_model=AnswerResponse)
def ask_question(request: QuestionRequest):
    answer = rag_interactor.answer_question(request.question)
    return {"answer": answer}
