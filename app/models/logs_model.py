from sqlalchemy import Sequence
from app.database.db import db

class Logs(db.Model):
    __tablename__ = 'PROCT_LOGS'

    id_log = db.Column(db.Integer, Sequence('procq_idlog'), primary_key=True)
    id_consulta = db.Column(db.Integer, db.ForeignKey('PROCT_CONSULTAS.id_consulta'), nullable=False)
    nmro_registros = db.Column(db.Integer, nullable=False)
    desc_error = db.Column(db.String(200), nullable=True)
    cant_segundos_ejecucion = db.Column(db.Float, nullable=False)
    fech_proceso = db.Column(db.Date, nullable=False)

    def __init__(self, id_consulta, nmro_registros, desc_error, cant_segundos_ejecucion, fech_proceso):
        self.id_consulta = id_consulta
        self.nmro_registros = nmro_registros
        self.desc_error = desc_error
        self.cant_segundos_ejecucion = cant_segundos_ejecucion
        self.fech_proceso = fech_proceso