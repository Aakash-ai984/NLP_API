from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from transformers import pipeline

router = APIRouter()
nlp_model = pipeline("text-generation", model="distilgpt2")

class TextRequest(BaseModel):
    prompt: str

@router.post("/generate")
def generate_text(request: TextRequest):
    if not request.prompt:
        raise HTTPException(status_code=400, detail="Prompt cannot be empty")
    result = nlp_model(request.prompt, max_length=50)
    return {"text": result[0]["generated_text"]}