from app.database.db import db

class Servicios(db.Model):
    __tablename__ = 'PROCT_SERVICIOS'

    id_servicio = db.Column(db.Integer, primary_key=True)
    alias = db.Column(db.String(10))
    id_area_responsable = db.Column(db.Integer, db.ForeignKey('PROCT_AREAS.id_area'))
    nomb_servicio = db.Column(db.String(30))
    desc_servicio = db.Column(db.String(100))
