from app.models.serv_ci_model import ServCIRelacion
from app.database.db import db

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
