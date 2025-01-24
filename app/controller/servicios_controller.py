from app.models.servicios_model import Servicios
from app.models.areas_model import Areas
from app.controller.areas_controller import getAllAreas
from app.database.db import db

class ServicioConArea:
    def __init__(self, id_servicio, alias, nomb_servicio, desc_servicio, nomb_area):
        self.id_servicio = id_servicio
        self.alias = alias
        self.nomb_servicio = nomb_servicio
        self.desc_servicio = desc_servicio
        self.nomb_area = nomb_area

def getAllServicios():
    resultados = (
        db.session.query(
            Servicios.id_servicio,
            Servicios.alias,
            Servicios.nomb_servicio,
            Servicios.desc_servicio,
            Areas.nombre  # Seleccionar el nombre del área
        )
        .join(Areas, Servicios.id_area_responsable == Areas.id_area, isouter=True)  # Hacer el JOIN
        .order_by(Servicios.id_servicio.asc())
        .all()
    )
    return [ServicioConArea(*row) for row in resultados]

def getServicioById(id):
    return Servicios.query.get_or_404(id)

def getCampos():
    areas = getAllAreas()
    opciones_areas = {area.id_area: area.nombre for area in areas}
    campos = [
        {"name": "alias", "type": "text", "label": "Alias", "required": True},
        {"name": "id_area_responsable", "type": "select", "label": "Área Responsable", "options": opciones_areas, "required": False},
        {"name": "nomb_servicio", "type": "text", "label": "Nombre del Servicio", "required": True},
        {"name": "desc_servicio", "type": "text", "label": "Descripción del Servicio", "required": False}
    ]
    return campos

def getDicValores():
    return {
        "id_servicio": "ID",
        "alias": "Alias",
        "nomb_servicio": "Nombre", 
        "nomb_area": "Área Responsable", 
        "desc_servicio": "Descripción"
    }

def getPK():
    servicio = Servicios(
        alias="TempAlias",
        id_area_responsable=1,
        nomb_servicio="Servicio Temporal",
        desc_servicio="Descripción del Servicio Temporal"
    )
    return servicio.pk_name

def postServicio(form):
    alias = form.get('alias')
    id_area_responsable = form.get('id_area_responsable')
    nomb_servicio = form.get('nomb_servicio')
    desc_servicio = form.get('desc_servicio')

    try:
        new_servicio = Servicios(alias=alias, id_area_responsable=id_area_responsable, nomb_servicio=nomb_servicio, desc_servicio=desc_servicio)
        db.session.add(new_servicio)
        db.session.commit()
        return {
            "estado": "éxito",
            "mensaje": "¡Servicio creado con éxito!",
        }
    except Exception as e:
        db.session.rollback()
        return {
            "estado": "error",
            "mensaje": f"¡Error al crear el Servicio: {str(e)}!"
        }
    
def deleteServicio(id):
    try:
        servicio = getServicioById(id)  # Si no existe, lanza un error 404

        db.session.delete(servicio)
        db.session.commit()

        return {
            "estado": "éxito",
            "mensaje": "¡Servicio eliminado con éxito!",
        }
    except Exception as e:
        db.session.rollback()
        return {
            "estado": "error",
            "mensaje": f"¡Error al eliminar el Servicio: {str(e)}!"
        }
    
def updateServicio(form, id):
    alias = form.get('alias')
    id_area_responsable = form.get('id_area_responsable')
    nomb_servicio = form.get('nomb_servicio')
    desc_servicio = form.get('desc_servicio')

    try:
        servicio_a_actualizar = getServicioById(id)
        if not servicio_a_actualizar:
            return {
                "estado": "error",
                "mensaje": "¡Servicio no encontrado!"
            }

        # Actualiza los campos del registro
        servicio_a_actualizar.alias = alias
        servicio_a_actualizar.id_area_responsable = id_area_responsable
        servicio_a_actualizar.nomb_servicio = nomb_servicio
        servicio_a_actualizar.desc_servicio = desc_servicio

        # Guarda los cambios en la base de datos
        db.session.commit()

        return {
            "estado": "éxito",
            "mensaje": "¡Servicio actualizado con éxito!"
        }

    except Exception as e:
        db.session.rollback()
        return {
            "estado": "error",
            "mensaje": f"¡Error al actualizar el Servicio: {str(e)}!"
        }