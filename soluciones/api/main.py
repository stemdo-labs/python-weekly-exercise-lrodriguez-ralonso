from fastapi import FastAPI
from datetime import date
from models import Persona

app = FastAPI()

@app.get("/personas")
async def get_personas():
    return {"message": "Hello, world"}

@app.get("/personas/{persona_id}")
async def get_persona(persona_id: int):
    return {"persona_id": persona_id}

@app.post("/personas/")
async def create_persona(persona: Persona):
    return persona

@app.put("/personas/{persona_id}")
async def update_persona(persona_id: int):
    return {"persona_id": persona_id}

@app.delete("/personas/{persona_id}")
async def delete_persona(persona_id: int):
    return {"persona_id": persona_id}