from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Reemplaza estos valores con los detalles de tu base de datos
USERNAME = 'tu_usuario'
PASSWORD = 'tu_contraseña'
HOST = 'tu_host'
PORT = 'tu_puerto'
SERVICE_NAME = 'tu_servicio'

# URL de conexión
DATABASE_URL = f'oracle+cx_oracle://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/?service_name={SERVICE_NAME}'

# Crear el motor de la base de datos
engine = create_engine(DATABASE_URL)

# Crear una sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base declarativa
Base = declarative_base()