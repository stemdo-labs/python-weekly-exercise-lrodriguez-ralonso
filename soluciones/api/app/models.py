from sqlalchemy import Column, Integer, String, Date

from db import Base

class Persona(Base):
    __tablename__ = "personas"

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    apellido = Column(String)
    edad = Column(String)
    fecha_nacimiento = Column(Date)