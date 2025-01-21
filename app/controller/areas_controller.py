from app.models.areas_model import Areas

def getAllAreas():
    return Areas.query.all()

def getCampos():
    campos = [
        {"name": "nombre", "type": "text", "label": "Nombre", "required": True},
        {"name": "empresa", "type": "text", "label": "Empresa", "required": True},
        {"name": "desc_area", "type": "text", "label": "Descripción", "required": True},
    ]
    return campos