from fastapi import FastAPI
from models import models

app = FastAPI()

def is_adult(age: int) -> bool:
    return age >= 18

@app.post("/user")
async def create_user(user: models.User):
    is_adult_ = is_adult(user.age)
    return {"name": user.name, "age": user.age, "is_adult": is_adult_}