from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import schemas, crud
from db import SessionLocal

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated [Session, Depends(get_db)]

@app.get("/personas")
async def read_personas(db: Session = Depends(get_db)):
    db_personas = crud.get_personas(db)
    return db_personas

@app.get("/personas/{persona_id}")
async def read_persona(persona_id: int, db: Session = Depends(get_db)):
    db_persona = crud.get_persona(db, persona_id)
    if db_persona is None:
        raise HTTPException(status_code=404, detail="Persona no encontrada")
    return db_persona


@app.post("/personas")
async def create_persona(persona: schemas.PersonaCreate, db: Session = Depends(get_db)):
    db_persona = crud.create_persona(db, persona)
    if db_persona is None:
        raise HTTPException(status_code=404, detail="Persona no encontrada")
    return db_persona

@app.put("/personas/{persona_id}")
async def update_persona(persona_id: int, persona_update: schemas.PersonaUpdate, db: Session = Depends(get_db)):
    db_persona = crud.update_persona(db, persona_id, persona_update)
    if db_persona is None:
        raise HTTPException(status_code=404, detail="Persona no encontrada")
    return db_persona

@app.delete("/personas/{persona_id}")
def delete_persona(persona_id: int, db: Session = Depends(get_db)):
    db_persona = crud.delete_persona(db, persona_id)
    if db_persona is None:
        raise HTTPException(status_code=404, detail="Persona no encontrada")
    return db_persona