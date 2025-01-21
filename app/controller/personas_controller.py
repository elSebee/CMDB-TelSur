from app.models.personas_model import Personas
from app.controller.areas_controller import getAllAreas

def getAllPersonas():
    return Personas.query.all()

def getCampos():
    areas = getAllAreas()
    opciones_areas = [area.nombre for area in areas]
    campos = [
        {"name": "rut", "type": "text", "label": "R.U.T", "required": True},
        {"name": "nomb_persona", "type": "text", "label": "Nombre", "required": True},
        {"name": "id_area", "type": "select", "label": "Área", "options": opciones_areas, "required": False},
        {"name": "desc_gerencia", "type": "text", "label": "Gerencia", "required": False},
        {"name": "desc_cargo", "type": "text", "label": "Cargo", "required": False},
        {"name": "mail", "type": "text", "label": "Correo Electrónico", "required": False},
        {"name": "celular", "type": "text", "label": "Número de Celular", "required": False},
        {"name": "codi_horario", "type": "text", "label": "Código de Horario", "required": False},
        {"name": "mtdo_aviso_default", "type": "select", "label": "Método de Aviso Predeterminado", "options": ["Mail", "Celular"], "required": False},
    ]
    return campos