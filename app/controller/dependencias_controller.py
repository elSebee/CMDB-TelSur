from app.models.dependencias_model import Dependencias
from app.controller.servicios_controller import getAllServicios
from app.controller.cis_controller import getAllCis

def getAllDependencias():
    dependencias = Dependencias.query.all()
    return dependencias

def getCampos():
    cis = getAllCis()
    opciones_ci = {ci.id_ci: ci.alias for ci in cis}
    servicios = getAllServicios()
    opciones_servicio = {servicio.id_servicio: servicio.alias for servicio in servicios}
    campos = [
        {"name": "id_ci_origen", "type": "select", "label": "CI Origen", "options": opciones_ci, "required": True},
        {"name": "id_ci_destino", "type": "select", "label": "CI Destino", "options": opciones_ci, "required": True},
        {"name": "id_servicio", "type": "select", "label": "ID Servicio", "options": opciones_servicio, "required": True},
        {"name": "tipo_relacion", "type": "text", "label": "Descripción Relación", "required": True},
    ]
    return campos

def getDicValores():
    return {
        "id_relacion": "ID Relación",
        "id_ci_origen": "CI Origen",
        "id_ci_destino": "CI Destino",
        "id_servicio": "ID Servicio",
        "tipo_relacion": "Descripción Relación"
    }

def getPK():
    dependencia = Dependencias(
        id_ci_origen=1,
        id_ci_destino=2,
        id_servicio=3,
        tipo_relacion="Relacion temporal"
    )

    return dependencia.pk_name
