from sqlalchemy import create_engine

#varible cadena de conexion
MARIADB_URL='mysql+pymysql://root:admin@localhost:3315/pyshop-3147246'
#Creal el objeto de conexion de la base de datos
engine = create_engine(MARIADB_URL)