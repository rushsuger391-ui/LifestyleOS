from fastapi import FastAPI
from agents import LifestyleAgent

app = FastAPI()
agent = LifestyleAgent()

@app.get("/")
def home():
    return {"message": "Lifestyle OS Backend Running"}

@app.post("/plan")
def generate_plan(data: dict):
    return agent.generate_plan(data)

