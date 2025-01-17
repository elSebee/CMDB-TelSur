import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SERVER_NAME = "localhost:7001"
    DEBUG = True

    # DATABASE_PATH = "app/database/contact_book.db"
    # DB_TOKEN = os.environ.get("DB_TOKEN", "")  # Para Encriptar la DB
    # ENCRYPT_DB = True

    TEMPLATE_FOLDER = "views/templates/"
    STATIC_FOLDER = "views/static/"