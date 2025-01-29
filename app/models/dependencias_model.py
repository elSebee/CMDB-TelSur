from sqlalchemy import Sequence
from app.database.db import db

class Dependencias(db.Model):
    __tablename__ = 'PROCT_DEPENDENCIAS'

    id_relacion = db.Column(db.Integer, Sequence('procq_iddependencias', metadata=db.metadata), primary_key=True)
    id_ci_origen = db.Column(db.Integer, db.ForeignKey('PROCT_CMDB_CONF_ITEMS.id_ci'), nullable=False)
    id_ci_destino = db.Column(db.Integer, db.ForeignKey('PROCT_CMDB_CONF_ITEMS.id_ci'), nullable=False)
    id_servicio = db.Column(db.Integer, db.ForeignKey('PROCT_SERVICIOS.id_servicio'), nullable=False)
    tipo_relacion = db.Column(db.String(30), nullable=False)

    def __init__(self, id_ci_origen, id_ci_destino, id_servicio, tipo_relacion):
        self.id_ci_origen = id_ci_origen
        self.id_ci_destino = id_ci_destino
        self.id_servicio = id_servicio
        self.tipo_relacion = tipo_relacion

    @property
    def pk_name(self):
        return 'id_relacion'
