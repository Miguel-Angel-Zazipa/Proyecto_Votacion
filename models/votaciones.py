from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime

class Votaciones(Base):
    __tablename__ = "votaciones"
    id = Column(Integer, primary_key=True)
    titulo = Column(String(100))
    descripcion = Column(Text)
    fecha_inicio = Column(DateTime)
    fecha_fin = Column(DateTime)
    usuario_creador_id = Column(Integer, ForeignKey("usuarios.id"))