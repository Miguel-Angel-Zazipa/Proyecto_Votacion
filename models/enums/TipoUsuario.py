#enum: Tipo de dato personalizado
#uso: Restringir Variables
#      solo algunos valores
from enum import Enum

class TipoUsuario(Enum):
    Usuario = "Usuario"
    Admin = "Administrador"