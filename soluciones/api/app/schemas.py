from datetime import date
from typing import Optional
from pydantic import BaseModel

class PersonaBase(BaseModel):
    nombre: str
    apellido: str
    edad: int
    fecha_nacimiento: date

class PersonaCreate(PersonaBase):
    id: int
    # Para permitir que esta clase sea utilizada para serializar y deserializar objetos ORM de SQLAlchemy
    class Config:
        orm_mode = True

class PersonaUpdate(PersonaBase):
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    edad: Optional[int] = None
    fecha_nacimiento: Optional[date] = None

class Persona(PersonaBase):
    id: int
    # Para permitir que esta clase sea utilizada para serializar y deserializar objetos ORM de SQLAlchemy
    class Config:
        orm_mode = True