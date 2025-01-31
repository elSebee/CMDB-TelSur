from app.database.db import db

class Avisos(db.Model):
    __tablename__ = 'PROCV_AVISOS_CONSULTAS'

    id_aviso = db.Column(db.Integer, primary_key=True)
    id_servicio = db.Column(db.Integer, nullable=False)
    nomb_servicio = db.Column(db.String(100), nullable=False)
    id_contexto = db.Column(db.String(100), nullable=False)
    id_consulta = db.Column(db.Integer, nullable=False)
    comentario_consulta = db.Column(db.String(1000), nullable=False)
    fech_aviso = db.Column(db.DateTime, nullable=False)
    cant_reintentos = db.Column(db.Integer, nullable=False)
    flag_resuelto = db.Column(db.String(10), nullable=False)
    flag_escalamiento = db.Column(db.String(10), nullable=False)

    def __init__(self, id_aviso, id_servicio, nomb_servicio, id_contexto, id_consulta, comentario_consulta, fech_aviso, cant_reintentos, flag_resuelto, flag_escalamiento):
        self.id_aviso = id_aviso
        self.id_servicio = id_servicio
        self.nomb_servicio = nomb_servicio
        self.id_contexto = id_contexto
        self.id_consulta = id_consulta
        self.comentario_consulta = comentario_consulta
        self.fech_aviso = fech_aviso
        self.cant_reintentos = cant_reintentos
        self.flag_resuelto = flag_resuelto
        self.flag_escalamiento = flag_escalamiento