from app.models.servicios_model import Servicios
from app.controller.areas_controller import getAllAreas

def getAllServicios():
    return Servicios.query.all()

def getCampos():
    areas = getAllAreas()
    opciones_areas = [area.nombre for area in areas]
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
        "id_area_responsable": "Área Responsable", 
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
