from app.database.db import db

class Personas(db.Model):
    __tablename__ = 'PROCT_PERSONAS'

    rut = db.Column(db.String(15), primary_key=True)
    nomb_persona = db.Column(db.String(50), nullable=True)
    id_area = db.Column(db.Integer, db.ForeignKey('PROCT_AREAS.id_area'), nullable=True)
    desc_gerencia = db.Column(db.String(100), nullable=True)
    desc_cargo = db.Column(db.String(100), nullable=True)
    mail = db.Column(db.String(50), nullable=True)
    celular = db.Column(db.Integer, nullable=True)
    codi_horario = db.Column(db.Integer, nullable=True)
    mtdo_aviso_default = db.Column(db.String(20), nullable=True)

    def __init__(self, rut, nomb_persona, id_area, desc_gerencia, desc_cargo, mail, celular, codi_horario, mtdo_aviso_default):
        self.rut = rut
        self.nomb_persona = nomb_persona
        self.id_area = id_area
        self.desc_gerencia = desc_gerencia
        self.desc_cargo = desc_cargo
        self.mail = mail
        self.celular = celular
        self.codi_horario = codi_horario
        self.mtdo_aviso_default = mtdo_aviso_default

    @property
    def pk_name(self):
        return 'rut'