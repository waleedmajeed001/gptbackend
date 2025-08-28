from fastapi import APIRouter
from pydantic import BaseModel

from services.llm import ask_gemini


router = APIRouter()


class ChatRequest(BaseModel):
    message: str


@router.post("/chat")
async def chat(req: ChatRequest):
    answer = ask_gemini(f"Answer based on TechTicks company info: {req.message}")
    return {"response": answer}


