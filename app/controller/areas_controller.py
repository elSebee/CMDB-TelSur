from app.models.areas_model import Areas
from app.database.db import db

def getAllAreas():
    return Areas.query.all()

def getAreaById(id):
    area = Areas.query.get_or_404(id)
    return area

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
        area = getAreaById(id)  # Si no existe, lanza un error 404

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
    
def updateArea(form, id_area):
    nombre = form.get('nombre')
    empresa = form.get('empresa')
    desc_area = form.get('desc_area')

    try:
        area_a_actualizar = getAreaById(id_area)
        if not area_a_actualizar:
            return {
                "estado": "error",
                "mensaje": "¡Área no encontrado!"
            }

        # Actualiza los campos del registro
        area_a_actualizar.nombre = nombre
        area_a_actualizar.empresa = empresa
        area_a_actualizar.desc_area = desc_area

        # Guarda los cambios en la base de datos
        db.session.commit()

        return {
            "estado": "éxito",
            "mensaje": "¡Área actualizada con éxito!"
        }

    except Exception as e:
        db.session.rollback()
        return {
            "estado": "error",
            "mensaje": f"¡Error al actualizar el Área: {str(e)}!"
        }