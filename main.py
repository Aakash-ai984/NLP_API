from fastapi import FastAPI, Depends, Request
from routes.text_processing import router
from utils.authentication import verify_api_key

app = FastAPI()
app.include_router(router)

@app.get("/")
def home():
    return {"message": "Welcome to NLP API"}

@app.get("/secure-nlp")
def secure_nlp(request: Request, _=Depends(verify_api_key)):
    return {"message": "You have accessed a protected NLP API!"}
