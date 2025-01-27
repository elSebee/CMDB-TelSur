from sqlalchemy import Sequence
from app.database.db import db

class Areas(db.Model):
    __tablename__ = 'PROCT_AREAS'

    id_area = db.Column(db.Integer, Sequence('procq_idareas', metadata=db.metadata), primary_key=True)
    nombre = db.Column(db.String(100), nullable=False, unique=True)
    desc_area = db.Column(db.String(800))
    empresa = db.Column(db.String(50))

    def __init__(self, nombre, empresa, desc_area):
        self.nombre = nombre
        self.empresa = empresa
        self.desc_area = desc_area

    @property
    def pk_name(self):
        return 'id_area'