from app.database.db import db

class Consultas(db.Model):
    __tablename__ = "PROCT_CONSULTAS"

    id_consulta = db.Column(db.Integer(), primary_key=True)
    id_servicio = db.Column(db.Integer, db.ForeignKey("PROCT_SERVICIOS.id_servicio"))
    desc_consulta = db.Column(db.Clob)
    id_tipo_consulta = db.Column(db.Integer)
    id_contexto = db.Column(db.String(100))
    fech_creacion = db.Column(db.Date)
    fech_fin_vigencia = db.Column(db.Date)
    codi_programacion = db.Column(db.Integer)
    nmro_max_error_log = db.Column(db.Integer)
    nmro_max_error_aviso = db.Column(db.Integer)
    comentario_consulta = db.Column(db.String(1000))
    cant_hrs_sgte_aviso = db.Column(db.Integer)

    def __init__(
        self,
        id_consulta,
        id_servicio,
        desc_consulta,
        id_tipo_consulta,
        id_contexto,
        fech_creacion,
        fech_fin_vigencia,
        codi_programacion,
        nmro_max_error_log,
        nmro_max_error_aviso,
        comentario_consulta,
        cant_hrs_sgte_aviso,
    ):
        self.id_consulta = id_consulta
        self.id_servicio = id_servicio
        self.desc_consulta = desc_consulta
        self.id_tipo_consulta = id_tipo_consulta
        self.id_contexto = id_contexto
        self.fech_creacion = fech_creacion
        self.fech_fin_vigencia = fech_fin_vigencia
        self.codi_programacion = codi_programacion
        self.nmro_max_error_log = nmro_max_error_log
        self.nmro_max_error_aviso = nmro_max_error_aviso
        self.comentario_consulta = comentario_consulta
        self.cant_hrs_sgte_aviso = cant_hrs_sgte_aviso
