from app.schemas.chat import ChatResponse

async def generate_answer(question: str) -> ChatResponse:
    answer = f"Respuesta bootstrap local para: {question}"
    return ChatResponse(answer=answer, provider="bootstrap-local")
