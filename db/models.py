from .database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text

class Usuarios(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50))
    apellido = Column(String(50))
    fecha_creacion = Column(DateTime)


class Credenciales(Base):
    __tablename__ = "credenciales"
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    tipo_usuario= Column(Integer)
    numero_cedula = Column(Integer, unique=True)
    correo = Column(String(100), unique=True)
    contrasena = Column(String(100))

class Votaciones(Base):
    __tablename__ = "votaciones"
    id = Column(Integer, primary_key=True)
    titulo = Column(String(100))
    descripcion = Column(Text)
    fecha_inicio = Column(DateTime)
    fecha_fin = Column(DateTime)
    usuario_creador_id = Column(Integer, ForeignKey("usuarios.id"))
 

class Tarjeton(Base):
    __tablename__ = "tarjeton"
    id = Column(Integer, primary_key=True)
    votacion_id = Column(Integer, ForeignKey("votaciones.id"))
    candidato_id = Column(Integer, ForeignKey("usuarios.id"))
    partido_politico= Column(Text)



class Votos(Base):
    __tablename__ = "votos"
    id = Column(Integer, primary_key=True)
    votante_id = Column(Integer, ForeignKey("usuarios.id"))
    candidato_id  = Column(Integer, ForeignKey("tarjeton.id"))
    fecha_voto = Column(DateTime)
