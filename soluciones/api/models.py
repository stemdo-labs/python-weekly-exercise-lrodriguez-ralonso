from pydantic import BaseModel

class Persona(BaseModel):
    id: int
    nombre: str
    apellidos: str
    edad: int
    fecha_nacimiento: str