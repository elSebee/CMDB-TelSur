from app.models.avisos_model import Avisos

def getAllAvisos():
    return Avisos.query.all()

def getDicValoresAvisos():
    return {
        "id_aviso": "ID",
        "id_servicio": "ID Servicio",
        "nomb_servicio": "Nombre Servicio",
        "id_contexto": "ID Contexto",
        "id_consulta": "ID Consulta",
        "comentario_consulta": "Comentario Consulta",
        "fech_aviso": "Fecha Aviso",
        "cant_reintentos": "Cant Reintentos",
        "flag_resuelto": "¿Resuelto?",
        "flag_escalamiento": "¿Escalamiento?"
    }