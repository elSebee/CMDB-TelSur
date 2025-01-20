import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SERVER_NAME = "localhost:7001"
    DEBUG = True

    # Configuración de la base de datos
    SQLALCHEMY_DATABASE_URI = (
        f'oracle+cx_oracle://{os.getenv("ORACLE_USER")}:{os.getenv("ORACLE_PASSWORD")}@'
        f'{os.getenv("ORACLE_HOST")}:{os.getenv("ORACLE_PORT")}/?service_name={os.getenv("ORACLE_SERVICE_NAME")}'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    TEMPLATE_FOLDER = "views/templates/"
    STATIC_FOLDER = "views/static/"
