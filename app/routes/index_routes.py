from flask import Blueprint, render_template
from app.controller.logs_controller import getAllLogs, getDicValoresLogs
from app.controller.avisos_controller import getAllAvisos, getDicValoresAvisos

alcance_global = Blueprint("menu", __name__)

@alcance_global.route("/", methods=['GET'])
def home():
    dic_valores_logs = getDicValoresLogs()
    dic_valores_avisos = getDicValoresAvisos()
    cabeceras_logs = list(dic_valores_logs.values())
    cabeceras_avisos = list(dic_valores_avisos.values())
    logs=getAllLogs()
    avisos=getAllAvisos()
    return render_template("index.html", valores_logs=logs, dic_valores_logs=dic_valores_logs, cabeceras_logs=cabeceras_logs,
                           valores_avisos=avisos, dic_valores_avisos=dic_valores_avisos, cabeceras_avisos=cabeceras_avisos)
