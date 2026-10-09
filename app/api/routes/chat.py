from fastapi import APIRouter
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.chat_service import generate_answer

router = APIRouter(prefix="/api/v1")

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    return await generate_answer(request.question)
