from sqlalchemy import Sequence
from app.controller.serv_ci_controller import getServCIbyCI
from app.database.db import db

class CMDBConfItems(db.Model):
    __tablename__ = 'PROCT_CMDB_CONF_ITEMS'

    id_ci = db.Column(db.Integer, Sequence('procq_idcmdb_conf_items', metadata=db.metadata), primary_key=True)
    alias = db.Column(db.String(100))
    prioridad = db.Column(db.String(10))
    tipo_ci = db.Column(db.String(30), nullable=False)
    estado = db.Column(db.String(15))
    fech_actualizacion = db.Column(db.Date)
    dire_ip = db.Column(db.String(15))
    puerto = db.Column(db.Integer)
    desc_ci = db.Column(db.String(200))
    url = db.Column(db.String(2000))

    __table_args__ = (
        db.CheckConstraint(
            "tipo_ci IN ('Servidor', 'Aplicación', 'Base de Datos', 'Web Service', 'Listener DB', 'Esquema', 'Sitio Web', 'Vista', 'Otros')",
            name='ck_tipo_ci'
        ),
    )
    
    def __init__(self, alias, prioridad, tipo_ci, estado, fech_actualizacion, dire_ip, puerto, desc_ci, url):
        self.alias = alias
        self.prioridad = prioridad
        self.tipo_ci = tipo_ci
        self.estado = estado
        self.fech_actualizacion = fech_actualizacion
        self.dire_ip = dire_ip
        self.puerto = puerto
        self.desc_ci = desc_ci
        self.url = url

    @property
    def pk_name(self):
        return 'id_ci'
    
    @property
    def relaciones(self):
        return getServCIbyCI(self.id_ci)