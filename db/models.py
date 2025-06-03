from .database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text

class Usuarios(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True)
    nombre_completo = Column(String(50))
    fecha_creacion = Column(DateTime)

class Credenciales(Base):
    __tablename__ = "credenciales"
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    correo = Column(String(100))
    contraseña = Column(String(100))

class Votaciones(Base):
    __tablename__ = "votaciones"
    id = Column(Integer, primary_key=True)
    titulo = Column(String(100))
    descripcion = Column(Text)
    fecha_inicio = Column(DateTime)
    fecha_fin = Column(DateTime)
    usuario_creador_id = Column(Integer, ForeignKey("usuarios.id"))

class Opciones(Base):
    __tablename__ = "opciones"
    id = Column(Integer, primary_key=True)
    votacion_id = Column(Integer, ForeignKey("votaciones.id"))
    texto_opcion = Column(String(100))

class Votos(Base):
    __tablename__ = "votos"
    id = Column(Integer, primary_key=True)
    usuarios_id = Column(Integer, ForeignKey("usuarios.id"))
    opcion_id = Column(Integer, ForeignKey("opciones.id"))
    fecha_voto = Column(DateTime)
