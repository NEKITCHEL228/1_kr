from fastapi import FastAPI
from models import models

app = FastAPI()

fake_bd = []

@app.post("/feedback")
async def send_feedback(feedback: models.Feedback):
    fake_bd.append(feedback)
    return {"message": "feedback sent"}