from app.models.logs_model import Logs
from sqlalchemy import func, asc
from datetime import datetime, timedelta

def getAllLogs():
    cinco_dias = datetime.now() - timedelta(days=5)

    logs = Logs.query.filter(
        func.trunc(Logs.fech_proceso) >= cinco_dias.date()
    ).order_by(asc(Logs.fech_proceso)).all()

    logs_list = []
    for log in logs:
        log_data = {
            'id_log': log.id_log,
            'id_consulta': log.id_consulta,
            'nmro_registros': log.nmro_registros,
            'desc_error': log.desc_error,
            'cant_segundos_ejecucion': log.cant_segundos_ejecucion,
            'fech_proceso': log.fech_proceso,
        }
        logs_list.append(log_data)

    return logs_list

def getDicValoresLogs():
    return {
        "id_log": "ID Log",
        "id_consulta": "ID Consulta",
        "nmro_registros": "Número Registros",
        "desc_error": "Descripción Error",
        "cant_segundos_ejecucion": "Segundos Ejecución",
        "fech_proceso": "Fecha Proceso",
    }
