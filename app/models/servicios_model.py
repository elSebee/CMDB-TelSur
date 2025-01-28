from sqlalchemy import Sequence
from app.database.db import db

class Servicios(db.Model):
    __tablename__ = 'PROCT_SERVICIOS'

    id_servicio = db.Column(db.Integer, Sequence('procq_idservicios', metadata=db.metadata), primary_key=True)
    alias = db.Column(db.String(30), nullable=False, unique=True)
    id_area_responsable = db.Column(db.Integer, db.ForeignKey('PROCT_AREAS.id_area'))
    nomb_servicio = db.Column(db.String(100))
    desc_servicio = db.Column(db.String(1000))

    def __init__(self, alias, id_area_responsable, nomb_servicio, desc_servicio):
        self.alias = alias
        self.id_area_responsable = id_area_responsable
        self.nomb_servicio = nomb_servicio
        self.desc_servicio = desc_servicio

    @property
    def pk_name(self):
        return 'id_servicio'