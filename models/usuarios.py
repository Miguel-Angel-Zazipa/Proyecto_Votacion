#importar modelo base
from db import Base
#importaciones sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text

class Usuarios(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50))
    apellido = Column(String(50))
    fecha_creacion = Column(DateTime)