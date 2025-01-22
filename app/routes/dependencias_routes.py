from flask import Blueprint, render_template

alcance_dependencias = Blueprint("dependencias", __name__)

@alcance_dependencias.route("/", methods=['GET'])
def dependencias():
    dic_valores = {
        "id_dependencia": "ID",
        "nombre_dependencia": "Nombre",
        "desc_dependencia": "Descripción"
    }
    cabeceras = list(dic_valores.values())
    cabeceras.insert(0, "Acción")
    dependencias = []
    return render_template("leer.html", breadcrumb="Dependencias", valores=dependencias, dic_valores=dic_valores, cabeceras=cabeceras, url_agregar="/dependencias/agregar")

@alcance_dependencias.route("/agregar", methods=['GET'])
def dependenciasAgregar():
    return render_template("agregar.html", breadcrumb="Dependencias", url_volver="/dependencias")