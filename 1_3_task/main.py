from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Nums(BaseModel):
    num1: int
    num2: int

@app.post("/calculate")
async def calculate(nums: Nums):
    return {"result": nums.num1 + nums.num2}
