from fastapi import FastAPI
from models import models

app = FastAPI()

user = models.User(name="Ваша имя и фамилия", id=1)

@app.get("/users")
async def get_users():
    return {"User_name": user.name, "User_id": user.id}