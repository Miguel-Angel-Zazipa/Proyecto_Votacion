from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Text
from datetime import datetime

class Tarjeton(Base):
    __tablename__ = "tarjeton"
    id = Column(Integer, primary_key=True)
    votacion_id = Column(Integer, ForeignKey("votaciones.id"))
    candidato_id = Column(Integer, ForeignKey("usuarios.id"))
    partido_politico= Column(Text)