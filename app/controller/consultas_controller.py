from app.models.consultas_model import Consultas
from app.database.db import db

def getAllConsultas():
    return Consultas.query.all()

def getCampos():
    campos = [
        {"name": "nombre", "type": "text", "label": "Nombre", "required": True},
        {"name": "empresa", "type": "text", "label": "Empresa", "required": True},
        {"name": "desc_area", "type": "text", "label": "Descripción", "required": True},
    ]
    return campos

def getDicValores():
    return {
        "id_consulta": "ID Consulta",
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
        id_consulta=1,  # Valor temporal para ID de la consulta
        id_servicio=100,  # Valor temporal para ID del servicio
        desc_consulta="Descripción temporal",  # Texto temporal para la descripción
        id_tipo_consulta=2,  # ID de tipo temporal
        id_contexto="Contexto temporal",  # Texto temporal para el contexto
        fech_creacion="2025-01-01",  # Fecha temporal
        fech_fin_vigencia="2025-12-31",  # Fecha temporal de fin de vigencia
        codi_programacion=12345,  # Código temporal de programación
        nmro_max_error_log=5,  # Número temporal de errores en el log
        nmro_max_error_aviso=3,  # Número temporal de errores para aviso
        comentario_consulta="Comentario temporal",  # Comentario temporal
        cant_hrs_sgte_aviso=24  # Cantidad temporal de horas para el siguiente aviso
    )
    return consulta.pk_name