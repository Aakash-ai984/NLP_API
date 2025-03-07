from fastapi import FastAPI
from routes.text_processing import router

app = FastAPI()
app.include_router(router)

@app.get("/")
def home():
    return {"message": "Welcome to the NLP API"}