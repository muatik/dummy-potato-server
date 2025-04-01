from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict
import uuid

app = FastAPI()

class Potato(BaseModel):
    id: str
    name: str
    weight: int

potatoes: Dict[str, Potato] = {}

@app.get("/api/v1/potatoes/{id}")
def get_potato(id: str):
    if id not in potatoes:
        raise HTTPException(status_code=404, detail="Potato not found")
    return potatoes[id]

@app.post("/api/v1/potatoes")
def create_potato(potato: Potato):
    if potato.id in potatoes:
        raise HTTPException(status_code=400, detail="Potato ID already exists")
    potatoes[potato.id] = potato
    return potato
