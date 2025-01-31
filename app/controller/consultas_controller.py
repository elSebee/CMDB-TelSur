from app.models.consultas_model import Consultas
from app.controller.servicios_controller import getAllServicios
from app.database.db import db
from datetime import datetime

def getAllConsultas():
    return Consultas.query.all()

def getConsultaById(id):
    consulta = Consultas.query.get_or_404(id)
    return consulta

def getCampos():
    servicios = getAllServicios()
    opciones_servicios = {servicio.id_servicio: servicio.alias for servicio in servicios}

    opciones_tipo_consulta = {
        1: 'query oracle', 
        2: 'webservice rest', 
        3: 'webservice soap', 
        4: 'comando sistema operativo'
    }

    opciones_codi_prog = {
        1 : 'automático', 
        2: 'manual'
    }

    campos = [
        {"name": "id_servicio", "type": "select", "label": "ID Servicio", "options": opciones_servicios,"required": True},
        {"name": "desc_consulta", "type": "text", "label": "Descripción Consulta", "required": True},
        {"name": "id_tipo_consulta", "type": "select", "label": "ID Tipo Consulta", "options": opciones_tipo_consulta, "required": True},
        {"name": "id_contexto", "type": "text", "label": "Contexto", "required": True},
        {"name": "fech_fin_vigencia", "type": "date", "label": "Fecha Fin Vigencia", "required": True},
        {"name": "codi_programacion", "type": "select", "label": "Código de Programación", "options": opciones_codi_prog,"required": True},
        {"name": "nmro_max_error_log", "type": "number", "label": "Max Errores en Log", "required": True},
        {"name": "nmro_max_error_aviso", "type": "number", "label": "Max Errores para Aviso", "required": True},
        {"name": "comentario_consulta", "type": "text", "label": "Comentario de la Consulta", "required": True},
        {"name": "cant_hrs_sgte_aviso", "type": "number", "label": "Cantidad Horas para Siguiente Aviso", "required": True},
    ]
    return campos

def getDicValores():
    return {
        "id_consulta": "ID",
        "id_servicio": "ID Servicio",
        "desc_consulta": "Descripción Consulta",
        "id_tipo_consulta": "ID Tipo Consulta",
        "id_contexto": "Contexto",
        "fech_creacion": "Fecha Creación",
        "fech_fin_vigencia": "Fecha Fin Vigencia",
        "codi_programacion": "Código de Programación",
        "nmro_max_error_log": "Max Errores en Log",
        "nmro_max_error_aviso": "Max Errores para Aviso",
        "comentario_consulta": "Comentario de la Consulta",
        "cant_hrs_sgte_aviso": "Cantidad Horas para Siguiente Aviso",
    }

def getPK():
    consulta =  Consultas(
        id_servicio=100,
        desc_consulta="Descripción temporal",
        id_tipo_consulta=2,
        id_contexto="Contexto temporal",
        fech_creacion="2025-01-01",
        fech_fin_vigencia="2025-12-31",
        codi_programacion=12345,
        nmro_max_error_log=5,
        nmro_max_error_aviso=3,
        comentario_consulta="Comentario temporal",
        cant_hrs_sgte_aviso=24
    )
    return consulta.pk_name

def postConsulta(form):
    id_servicio = form.get('id_servicio')
    desc_consulta = form.get('desc_consulta')
    id_tipo_consulta = form.get('id_tipo_consulta')
    id_contexto = form.get('id_contexto')
    fech_creacion = datetime.today().date()
    fech_fin_vigencia_str = form.get('fech_fin_vigencia')
    fech_fin_vigencia = datetime.strptime(fech_fin_vigencia_str, "%d-%m-%Y").date()
    codi_programacion = form.get('codi_programacion')
    nmro_max_error_log = form.get('nmro_max_error_log')
    nmro_max_error_aviso = form.get('nmro_max_error_aviso')
    comentario_consulta = form.get('comentario_consulta')
    cant_hrs_sgte_aviso = form.get('cant_hrs_sgte_aviso')

    try:
        new_consulta = Consultas(
            id_servicio=id_servicio,
            desc_consulta=desc_consulta,
            id_tipo_consulta=id_tipo_consulta,
            id_contexto=id_contexto,
            fech_creacion=fech_creacion,
            fech_fin_vigencia=fech_fin_vigencia,
            codi_programacion=codi_programacion,
            nmro_max_error_log=nmro_max_error_log,
            nmro_max_error_aviso=nmro_max_error_aviso,
            comentario_consulta=comentario_consulta,
            cant_hrs_sgte_aviso=cant_hrs_sgte_aviso
        )
        db.session.add(new_consulta)
        db.session.commit()
        return {
            "estado": "éxito",
            "mensaje": "¡Consulta creada con éxito!",
        }
    except Exception as e:
        db.session.rollback()
        return {
            "estado": "error",
            "mensaje": f"¡Error al crear la Consulta: {str(e)}!"
        }
    
def deleteConsulta(id):
    try:
        consulta = getConsultaById(id)  # Si no existe, lanza un error 404

        db.session.delete(consulta)
        db.session.commit()

        return {
            "estado": "éxito",
            "mensaje": "¡Consulta eliminada con éxito!",
        }
    except Exception as e:
        db.session.rollback()
        return {
            "estado": "error",
            "mensaje": f"¡Error al eliminar la Consulta: {str(e)}!"
        }

def updateConsulta(form, id_ci):
    id_servicio = form.get('id_servicio')
    desc_consulta = form.get('desc_consulta')
    id_tipo_consulta = form.get('id_tipo_consulta')
    id_contexto = form.get('id_contexto')
    fech_creacion = datetime.today().date()
    fech_fin_vigencia_str = form.get('fech_fin_vigencia')
    fech_fin_vigencia = datetime.strptime(fech_fin_vigencia_str, "%d-%m-%Y").date()
    codi_programacion = form.get('codi_programacion')
    nmro_max_error_log = form.get('nmro_max_error_log')
    nmro_max_error_aviso = form.get('nmro_max_error_aviso')
    comentario_consulta = form.get('comentario_consulta')
    cant_hrs_sgte_aviso = form.get('cant_hrs_sgte_aviso')

    try:
        consulta_a_actualizar = getConsultaById(id_ci)
        if not consulta_a_actualizar:
            return {
                "estado": "error",
                "mensaje": "¡Consulta no encontrada!"
            }

        # Actualiza los campos del registro
        consulta_a_actualizar.id_servicio = id_servicio,
        consulta_a_actualizar.desc_consulta = desc_consulta,
        consulta_a_actualizar.id_tipo_consulta = id_tipo_consulta,
        consulta_a_actualizar.id_contexto = id_contexto,
        consulta_a_actualizar.fech_creacion = fech_creacion,
        consulta_a_actualizar.fech_fin_vigencia = fech_fin_vigencia,
        consulta_a_actualizar.codi_programacion = codi_programacion,
        consulta_a_actualizar.nmro_max_error_log = nmro_max_error_log,
        consulta_a_actualizar.nmro_max_error_aviso = nmro_max_error_aviso,
        consulta_a_actualizar.comentario_consulta = comentario_consulta,
        consulta_a_actualizar.cant_hrs_sgte_aviso = cant_hrs_sgte_aviso

        # Guarda los cambios en la base de datos
        db.session.commit()

        return {
            "estado": "éxito",
            "mensaje": "¡Consulta actualizada con éxito!"
        }
    
    except Exception as e:
        db.session.rollback()
        return {
            "estado": "error",
            "mensaje": f"¡Error al actualizar la Consulta: {str(e)}!"
        }