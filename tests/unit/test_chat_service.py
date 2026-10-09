import pytest
from app.services.chat_service import generate_answer

@pytest.mark.asyncio
async def test_generate_answer_known_question():
    result = await generate_answer("¿Qué es FastAPI?")
    assert result.answer.startswith("Respuesta bootstrap local para:")
    assert result.provider == "bootstrap-local"
