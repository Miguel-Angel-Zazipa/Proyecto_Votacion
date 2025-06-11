from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime

class Votos(Base):
    __tablename__ = "votos"
    id = Column(Integer, primary_key=True)
    votante_id = Column(Integer, ForeignKey("usuarios.id"))
    candidato_id  = Column(Integer, ForeignKey("tarjeton.id"))
    fecha_voto = Column(DateTime)