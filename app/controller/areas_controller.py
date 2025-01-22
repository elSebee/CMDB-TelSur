from app.models.areas_model import Areas
from app.database.db import db

def getAllAreas():
    return Areas.query.all()

def getCampos():
    campos = [
        {"name": "nombre", "type": "text", "label": "Nombre", "required": True},
        {"name": "empresa", "type": "text", "label": "Empresa", "required": True},
        {"name": "desc_area", "type": "text", "label": "Descripción", "required": True},
    ]
    return campos

def postArea(nombre, empresa, desc_area):
    try:
        new_area = Areas(nombre=nombre, empresa=empresa, desc_area=desc_area)
        db.session.add(new_area)
        db.session.commit()
        return {
            "estado": "éxito",
            "mensaje": "Área creada con éxito",
            "area": {
                "nombre": new_area.nombre,
                "empresa": new_area.empresa,
                "desc_area": new_area.desc_area,
            },
        }
    except Exception as e:
        db.session.rollback()
        return {
            "estado": "error",
            "mensaje": f"Error al crear el área: {str(e)}"
        }