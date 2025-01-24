from app.models.personas_model import Personas
from app.models.areas_model import Areas
from app.controller.areas_controller import getAllAreas
from app.database.db import db
from sqlalchemy import asc

class PersonaConArea:
    def __init__(self, rut, nomb_persona, nomb_area, desc_gerencia, desc_cargo, mail, celular, codi_horario, mtdo_aviso_default):
        self.rut = rut
        self.nomb_persona = nomb_persona
        self.nomb_area = nomb_area
        self.desc_gerencia = desc_gerencia
        self.desc_cargo = desc_cargo
        self.mail = mail
        self.celular = celular
        self.codi_horario = codi_horario
        self.mtdo_aviso_default = mtdo_aviso_default

def getAllPersonas():
    resultados = (
        db.session.query(
            Personas.rut,
            Personas.nomb_persona,
            Personas.desc_gerencia,
            Personas.desc_cargo,
            Personas.mail,
            Personas.celular,
            Personas.codi_horario,
            Personas.mtdo_aviso_default,
            Areas.nombre,  # Seleccionar el nombre del área
        )
        .join(Areas, Personas.id_area == Areas.id_area, isouter=True)  # Hacer el JOIN
        .order_by(asc(Personas.nomb_persona))
        .all()
    )
    return [PersonaConArea(*row) for row in resultados]

def getPersonaById(id):
    return Personas.query.get_or_404(id)

def getCampos():
    areas = getAllAreas()
    opciones_areas = {area.id_area: area.nombre for area in areas}
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

def getDicValores():
    return {
        "rut": "R.U.T",
        "nomb_persona": "Nombre",
        "id_area": "Área", 
        "desc_cargo": "Cargo", 
        "mail": "Mail", 
        "celular": "Teléfono", 
        "mtdo_aviso_default": "Método Aviso"
    }

def getPK():
    persona = Personas(
        rut="12345678-9",
        nomb_persona="Nombre Temporal",
        id_area=1,
        desc_gerencia="Gerencia Temporal",
        desc_cargo="Cargo Temporal",
        mail="correo@temporal.com",
        celular=987654321,
        codi_horario=1234,
        mtdo_aviso_default="Email"
    )
    return persona.pk_name

def postPersona(form):
    rut = form.get('rut')
    nomb_persona = form.get('nomb_persona')
    id_area = form.get('id_area')
    desc_gerencia = form.get('desc_gerencia')
    desc_cargo = form.get('desc_cargo')
    mail = form.get('mail')
    celular = form.get('celular')
    codi_horario = form.get('codi_horario')
    mtdo_aviso_default = form.get('mtdo_aviso_default')

    try:
        new_persona = Personas(rut=rut, nomb_persona=nomb_persona, id_area=id_area, desc_gerencia=desc_gerencia, desc_cargo=desc_cargo, mail=mail, celular=celular, codi_horario=codi_horario, mtdo_aviso_default=mtdo_aviso_default)
        db.session.add(new_persona)
        db.session.commit()
        return {
            "estado": "éxito",
            "mensaje": "¡Persona creada con éxito!",
        }
    except Exception as e:
        db.session.rollback()
        return {
            "estado": "error",
            "mensaje": f"¡Error al crear la Persona: {str(e)}!"
        }
    
def deletePersona(id):
    try:
        persona = getPersonaById(id)  # Si no existe, lanza un error 404

        db.session.delete(persona)
        db.session.commit()

        return {
            "estado": "éxito",
            "mensaje": "¡Persona eliminada con éxito!",
        }
    except Exception as e:
        db.session.rollback()
        return {
            "estado": "error",
            "mensaje": f"¡Error al eliminar la Persona: {str(e)}!"
        }
    
def updatePersona(form, id):
    rut = form.get('rut')
    nomb_persona = form.get('nomb_persona')
    id_area = form.get('id_area')
    desc_gerencia = form.get('desc_gerencia')
    desc_cargo = form.get('desc_cargo')
    mail = form.get('mail')
    celular = form.get('celular')
    codi_horario = form.get('codi_horario')
    mtdo_aviso_default = form.get('mtdo_aviso_default')

    try:
        persona_a_actualizar = getPersonaById(id)
        if not persona_a_actualizar:
            return {
                "estado": "error",
                "mensaje": "!Persona no encontrada!"
            }
        
        persona_a_actualizar.rut = rut
        persona_a_actualizar.nomb_persona = nomb_persona
        persona_a_actualizar.id_area = id_area
        persona_a_actualizar.desc_gerencia = desc_gerencia
        persona_a_actualizar.desc_cargo = desc_cargo
        persona_a_actualizar.mail = mail
        persona_a_actualizar.celular = celular
        persona_a_actualizar.codi_horario = codi_horario
        persona_a_actualizar.mtdo_aviso_default = mtdo_aviso_default

        # Guarda los cambios en la base de datos
        db.session.commit()

        return {
            "estado": "éxito",
            "mensaje": "¡Persona actualizada con éxito!"
        }

    except Exception as e:
        db.session.rollback()
        return {
            "estado": "error",
            "mensaje": f"¡Error al actualizar la Persona: {str(e)}!"
        }