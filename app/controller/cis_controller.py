from app.models.cis_model import CMDBConfItems
from app.controller.servicios_controller import getAllServicios
from app.controller.serv_ci_controller import postServCI, updateServCI
from app.database.db import db
from datetime import datetime

def getAllCis():
    cis = CMDBConfItems.query.order_by(CMDBConfItems.id_ci.asc()).all()
    return cis

def getCiById(id):
    ci = CMDBConfItems.query.get_or_404(id)
    return ci

def getCampos():
    servicios = getAllServicios()
    opciones_servicios = {servicio.id_servicio: servicio.alias for servicio in servicios}
    campos = [
        {"name": "alias", "type": "text", "label": "Alias", "required": True},
        {"name": "prioridad", "type": "select", "label": "Prioridad", "options": ["Alta", "Media", "Baja"], "required": True},
        {"name": "tipo_ci", "type": "select", "label": "Tipo", "options": ['Servidor', 'Aplicación', 'Base de Datos', 'Web Service', 'Listener DB', 'Esquema', 'Sitio Web', 'Vista', 'Otros'], "required": True},
        {"name": "estado", "type": "select", "label": "Estado", "options": ["Activo", "Inactivo", "En mantenimiento"], "required": True},
        {"name": "dire_ip", "type": "text", "label": "Dirección IP", "required": False},
        {"name": "puerto", "type": "number", "label": "Puerto", "required": False},
        {"name": "url", "type": "text", "label": "URL", "required": False},
        {"name": "desc_ci", "type": "text", "label": "Descripción", "required": False},
        {"name": "serv_ci", "type": "checkbox", "label": "Servicios Involucrados", "options": opciones_servicios, "required": True}
    ]
    return campos

def getDicValores():
    return {
        "id_ci": "ID",
        "alias": "Alias",
        "prioridad": "Prioridad", 
        "tipo_ci": "Tipo", 
        "estado": "Estado", 
        "dire_ip": "Dirección IP", 
        "puerto": "Puerto", 
        "fech_actualizacion": "Fecha", 
        "url": "URL", 
        "desc_ci": "Descripción"
    }

def getPK():
    ci = CMDBConfItems(
        alias="Temporal Alias",
        prioridad="Alta",
        tipo_ci="Servidor",
        estado="Activo",
        fech_actualizacion="2023-01-23",
        dire_ip="192.168.1.1",
        puerto=8080,
        desc_ci="Descripción temporal",
        url="http://temporal-url.com"
    )

    return ci.pk_name

def postCI(form):
    alias = form.get('alias')
    prioridad = form.get('prioridad')
    tipo_ci = form.get('tipo_ci')
    estado = form.get('estado')
    fech_actualizacion = datetime.today().date()
    dire_ip = form.get('dire_ip')
    puerto = form.get('puerto')
    desc_ci = form.get('desc_ci')
    url = form.get('url')
    serv_ci = form.getlist('serv_ci')
    desc_relacion = form.get('desc_relacion')
    try:
        new_ci = CMDBConfItems(
            alias=alias,
            prioridad=prioridad,
            tipo_ci=tipo_ci,
            estado=estado,
            fech_actualizacion=fech_actualizacion,
            dire_ip=dire_ip,
            puerto=puerto,
            desc_ci=desc_ci,
            url=url
        )
        db.session.add(new_ci)
        db.session.commit()

        id_ci = new_ci.id_ci
        crear_serv_ci = postServCI(id_ci, serv_ci, desc_relacion)

        if crear_serv_ci['estado'] == 'error':
            return {
                "estado": "error",
                "mensaje": crear_serv_ci['mensaje']
            }

        return {
            "estado": "éxito",
            "mensaje": "¡Item de Configuración creado con éxito!"
        }
    except Exception as e:
        db.session.rollback()
        return {
            "estado": "error",
            "mensaje": f"¡Error al crear el Item: {str(e)}!"
        }
    
def deleteCI(id):
    try:
        ci = CMDBConfItems.query.get_or_404(id)  # Si no existe, lanza un error 404

        db.session.delete(ci)
        db.session.commit()

        return {
            "estado": "éxito",
            "mensaje": "¡Item de Configuración eliminado con éxito!",
        }
    except Exception as e:
        db.session.rollback()
        return {
            "estado": "error",
            "mensaje": f"¡Error al eliminar el Item: {str(e)}!"
        }
    

def updateCI(form, id_ci):
    alias = form.get('alias')
    prioridad = form.get('prioridad')
    tipo_ci = form.get('tipo_ci')
    estado = form.get('estado')
    fech_actualizacion = datetime.today().date()
    dire_ip = form.get('dire_ip')
    puerto = form.get('puerto')
    desc_ci = form.get('desc_ci')
    url = form.get('url')
    serv_ci = form.getlist('serv_ci')
    desc_relacion = form.get('desc_relacion')

    try:
        ci_a_actualizar = getCiById(id_ci)
        if not ci_a_actualizar:
            return {
                "estado": "error",
                "mensaje": "¡Item de Configuración no encontrado!"
            }

        # Actualiza los campos del registro
        ci_a_actualizar.alias = alias
        ci_a_actualizar.prioridad = prioridad
        ci_a_actualizar.tipo_ci = tipo_ci
        ci_a_actualizar.estado = estado
        ci_a_actualizar.fech_actualizacion = fech_actualizacion
        ci_a_actualizar.dire_ip = dire_ip
        ci_a_actualizar.puerto = puerto
        ci_a_actualizar.desc_ci = desc_ci
        ci_a_actualizar.url = url

        # Guarda los cambios en la base de datos
        db.session.commit()

        actualizar_serv_ci = updateServCI(id_ci, serv_ci, desc_relacion)

        if actualizar_serv_ci['estado'] == 'error':
            return {
                "estado": "error",
                "mensaje": actualizar_serv_ci['mensaje']
            }

        return {
            "estado": "éxito",
            "mensaje": "¡Item de Configuración actualizado con éxito!"
        }
    
    except Exception as e:
        db.session.rollback()
        return {
            "estado": "error",
            "mensaje": f"¡Error al actualizar el Item: {str(e)}!"
        }