from app.models.serv_ci_model import ServCIRelacion
from app.models.servicios_model import Servicios
from app.database.db import db

class ServsCIs:
    def __init__(self, id_ci, id_servicio, alias):
        self.id_ci = id_ci
        self.id_servicio = id_servicio
        self.alias = alias

def getAllServCI():
    serv_ci = (
        db.session.query(ServCIRelacion.id_ci, ServCIRelacion.id_servicio, Servicios.alias)
        .join(Servicios, ServCIRelacion.id_servicio == Servicios.id_servicio)
        .order_by(ServCIRelacion.id_ci.asc())
        .all()
    )
    
    return [ServsCIs(*row) for row in serv_ci]

def getServCIbyCI(id_ci):
    relaciones = ServCIRelacion.query.filter_by(id_ci=id_ci).all()
    return relaciones    

def postServCI(id_ci, serv_ci, desc_relacion):
    try:
        relaciones_creadas = 0

        # Crear registros en la tabla ServCIRelacion
        for id_servicio in serv_ci:
            new_serv_ci = ServCIRelacion(id_servicio=id_servicio, id_ci=id_ci, desc_relacion=desc_relacion)
            db.session.add(new_serv_ci)
            db.session.commit()
            relaciones_creadas += 1

        return {
            "estado": "éxito",
            "mensaje": f"Se crearon {relaciones_creadas} relaciones en ServCIRelacion.",
        }

    except Exception as e:
        db.session.rollback()
        return {
            "estado": "error",
            "mensaje": f"¡Error al crear la relación: {str(e)}!"
        }
    

def updateServCI(id_ci, serv_ci, desc_relacion):
    try:
        # Eliminar todas las relaciones existentes para este CI
        ServCIRelacion.query.filter_by(id_ci=id_ci).delete()

        crear = postServCI(id_ci, serv_ci, desc_relacion)

        if crear["estado"] == "error":
            raise Exception(crear["mensaje"])

        return {
            "estado": "éxito",
            "mensaje": f"Se actualizaron las relaciones en ServCIRelacion.",
        }

    except Exception as e:
        db.session.rollback()
        return {
            "estado": "error",
            "mensaje": f"¡Error al actualizar las relaciones: {str(e)}!"
        }
