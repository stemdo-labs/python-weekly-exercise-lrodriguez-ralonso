from sqlalchemy.orm import Session

import model, schema

def get_personas(db: Session):
    return db.query(model.Persona).all()

def get_persona(db: Session, persona_id: int):
    return db.query(model.Persona).filter(persona_id == model.Persona.id).first()

def create_persona(db: Session, persona: schema.PersonaCreate):
    db_persona = model.Persona(nombre=persona.nombre, apellido=persona.apellido, fecha_nacimiento=persona.fecha_nacimiento, edad=persona.edad)
    db.add(db_persona)
    db.commit()
    db.refresh()
    return db_persona

def update_persona(db: Session, persona_id: int, persona_update: schema.PersonaUpdate):
    db_persona = db.query(model.Persona).filter(model.Persona.id == persona_id).first()

    if db_persona is None:
        return None
    
    for attr, value in persona_update.model_dump().items():
        if value is not None:
            setattr(db_persona, attr, value)
            
    db.commit()
    db.refresh(db_persona)
    return db_persona

def delete_persona(db: Session, persona_id: int):
    db_persona = db.query(model.Persona).filter(model.Persona.id == persona_id).first()
    
    if db_persona is None:
        return None

    db.delete(db_persona)
    db.commit()

    return db_persona