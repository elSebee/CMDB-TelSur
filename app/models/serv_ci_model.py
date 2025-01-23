from app.database.db import db

class ServCIRelacion(db.Model):
    __tablename__ = 'PROCT_SERV_CI'

    id_servicio = db.Column(db.Integer, db.ForeignKey('PROCT_SERVICIOS.id_servicio'), primary_key=True, nullable=False)
    id_ci = db.Column(db.Integer, db.ForeignKey('PROCT_CMDB_CONF_ITEMS.id_ci'), primary_key=True, nullable=False)
    desc_relacion = db.Column(db.String(200))

    def __init__(self, id_servicio, id_ci, desc_relacion):
        self.id_servicio = id_servicio
        self.id_ci = id_ci
        self.desc_relacion = desc_relacion

    @property
    def pk_name(self):
        return ('id_servicio', 'id_ci')