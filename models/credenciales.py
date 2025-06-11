from db import Base
from sqlalchemy import Enum, Column, Integer, String, ForeignKey
from models.enums import TipoUsuario

class Credenciales(Base):
    __tablename__ = "credenciales"
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    tipo_usuario= Column(Enum(TipoUsuario))
    numero_cedula = Column(Integer, unique=True)
    correo = Column(String(100), unique=True)
    contrasena = Column(String(100))