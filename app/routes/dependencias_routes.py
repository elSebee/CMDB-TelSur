from flask import Blueprint, render_template
from app.controller.dependencias_controller import getAllDependencias, getDicValores, getPK, getCampos

alcance_dependencias = Blueprint("dependencias", __name__)

@alcance_dependencias.route("/", methods=['GET'])
def dependencias():
    dic_valores = getDicValores()
    cabeceras = list(dic_valores.values())
    cabeceras.insert(0, "Acción")
    dependencias=getAllDependencias()
    pk=getPK()
    return render_template("leer.html", breadcrumb="Dependencias", valores=dependencias, dic_valores=dic_valores, cabeceras=cabeceras, pk=pk, url='dependencias')

@alcance_dependencias.route("/agregar", methods=['GET'])
def agregar():
    campos = getCampos()
    return render_template("agregarDependencia.html", breadcrumb="Dependencias", campos=campos, url='dependencias')