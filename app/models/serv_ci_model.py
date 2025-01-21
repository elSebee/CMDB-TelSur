from app import db
class ServCIRelacion(db.Model):
    __tablename__ = 'PROCT_SERV_CI'

    id_servicio = db.Column(db.Integer, db.ForeignKey('PROCT_SERVICIOS.id_servicio'), primary_key=True, nullable=False)
    id_ci = db.Column(db.Integer, db.ForeignKey('PROCT_CMDB_CONF_ITEMS.id_ci'), primary_key=True, nullable=False)
    desc_relacion = db.Column(db.String(200))