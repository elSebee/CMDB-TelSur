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

def getDicValores():
    return {
        "id_area": "ID",
        "nombre": "Nombre",
        "empresa": "Empresa",
        "desc_area": "Descripción"
    }

def getPK():
    area = Areas(nombre="temporal", empresa="temporal", desc_area="temporal")
    return area.pk_name

def postArea(form):
    nombre = form.get('nombre')
    empresa = form.get('empresa')
    desc_area = form.get('desc_area')
    try:
        new_area = Areas(nombre=nombre, empresa=empresa, desc_area=desc_area)
        db.session.add(new_area)
        db.session.commit()
        return {
            "estado": "éxito",
            "mensaje": "¡Área creada con éxito!",
        }
    except Exception as e:
        db.session.rollback()
        return {
            "estado": "error",
            "mensaje": f"¡Error al crear el Área: {str(e)}!"
        }
    
def deleteArea(id):
    try:
        area = Areas.query.get_or_404(id)  # Si no existe, lanza un error 404

        db.session.delete(area)
        db.session.commit()

        return {
            "estado": "éxito",
            "mensaje": "¡Área eliminada con éxito!",
        }
    except Exception as e:
        db.session.rollback()
        return {
            "estado": "error",
            "mensaje": f"¡Error al eliminar el Área: {str(e)}!"
        }