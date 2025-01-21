from flask import Blueprint, render_template

alcance_dependencias = Blueprint("dependencias", __name__)

@alcance_dependencias.route("/", methods=['GET'])
def dependencias():
    ids = ["Acción", "ID", "", "", "", "", "", "", "", ""]
    dependencias = []
    return render_template("leer.html", breadcrumb="Dependencias", valores=dependencias, ids=ids, url_agregar="/dependencias/agregar")

@alcance_dependencias.route("/agregar", methods=['GET'])
def dependenciasAgregar():
    return render_template("agregar.html", breadcrumb="Dependencias", url_volver="/dependencias")