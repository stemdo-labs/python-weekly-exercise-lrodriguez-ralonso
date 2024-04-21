from sqlalchemy.orm import Session

import models, schemas

def get_personas(db: Session):
    return db.query(models.Persona).all()

def get_persona(db: Session, persona_id: int):
    return db.query(models.Persona).filter(persona_id == models.Persona.id).first()

def create_persona(db: Session, persona: schemas.PersonaCreate):
    db_persona = models.Persona(id=persona.id, nombre=persona.nombre, apellido=persona.apellido, fecha_nacimiento=persona.fecha_nacimiento, edad=persona.edad)
    db.add(db_persona)
    db.commit()
    db.refresh(db_persona)
    return db_persona

def update_persona(db: Session, persona_id: int, persona_update: schemas.PersonaUpdate):
    db_persona = db.query(models.Persona).filter(models.Persona.id == persona_id).first()

    if db_persona is None:
        return None
    
    for attr, value in vars(persona_update).items():
        if value is not None:
            setattr(db_persona, attr, value)
            
    db.commit()
    db.refresh(db_persona)
    return db_persona

def delete_persona(db: Session, persona_id: int):
    db_persona = db.query(models.Persona).filter(models.Persona.id == persona_id).first()
    
    if db_persona is None:
        return None

    db.delete(db_persona)
    db.commit()

    return db_persona