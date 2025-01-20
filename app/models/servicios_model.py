from sqlalchemy import Column, Integer, String
from .database.db_oracle import Base

class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)