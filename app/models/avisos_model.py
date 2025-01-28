from app.database.db import db

class Avisos(db.Model):
    __tablename__ = 'PROCT_AVISOS'

    id_aviso = db.Column(db.Integer, primary_key=True)
    id_consulta = db.Column(db.Integer, nullable=False)
    fech_aviso = db.Column(db.Date, nullable=False)
    cant_reintentos = db.Column(db.Integer, nullable=False)
    flag_resuelto = db.Column(db.String(10), nullable=False)
    flag_escalamiento = db.Column(db.String(10), nullable=False)

    def __init__(self, id_aviso, id_consulta, fech_aviso, cant_reintentos, flag_resuelto, flag_escalamiento):
        self.id_aviso = id_aviso
        self.id_consulta = id_consulta
        self.fech_aviso = fech_aviso
        self.cant_reintentos = cant_reintentos
        self.flag_resuelto = flag_resuelto
        self.flag_escalamiento = flag_escalamiento