from app.models.cis_model import CMDBConfItems
from app.controller.servicios_controller import getAllServicios

def getAllCis():
    return CMDBConfItems.query.all()

def getCampos():
    servicios = getAllServicios()
    opciones_servicios = [servicio.alias for servicio in servicios]
    campos = [
        {"name": "alias", "type": "text", "label": "Alias", "required": True},
        {"name": "prioridad", "type": "select", "label": "Prioridad", "options": ["Alta", "Media", "Baja"], "required": True},
        {"name": "tipo_ci", "type": "select", "label": "Tipo", "options": ['Servidor', 'Aplicación', 'Base de Datos', 'Web Service', 'Listener DB', 'Esquema', 'Sitio Web', 'Vista', 'Otros'], "required": True},
        {"name": "estado", "type": "select", "label": "Estado", "options": ["Activo", "Inactivo", "En mantenimiento"], "required": True},
        {"name": "dire_ip", "type": "text", "label": "Dirección IP", "required": False},
        {"name": "url", "type": "text", "label": "URL", "required": False},
        {"name": "desc_ci", "type": "text", "label": "Descripción", "required": False},
        {"name": "serv_ci", "type": "checkbox", "label": "Servicios Involucrados", "options": opciones_servicios, "required": True}
    ]
    return campos