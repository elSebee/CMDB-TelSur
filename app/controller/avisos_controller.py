from app.models.avisos_model import Avisos

def getAllAvisos():
    return Avisos.query.all()

def getDicValoresAvisos():
    return {
        "id_aviso": "ID Aviso",
        "id_consulta": "ID Consulta",
        "fech_aviso": "Fecha Aviso",
        "cant_reintentos": "Cantidad de Reintentos",
        "flag_resuelto": "¿Resuelto?",
        "flag_escalamiento": "¿Escalamiento?",
    }