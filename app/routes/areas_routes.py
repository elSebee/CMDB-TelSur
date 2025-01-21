from flask import Blueprint, render_template

alcance_areas = Blueprint("areas", __name__)

@alcance_areas.route("/", methods=['GET'])
def areas():
    ids = ["Acción", "ID", "Nombre", "Empresa", "Descripción"]
    areas=[]
    return render_template("leer.html", breadcrumb="Áreas", valores=areas, ids=ids, url_agregar="/areas/agregar")

@alcance_areas.route("/agregar", methods=['GET'])
def areasAgregar():
    return render_template("agregar.html", breadcrumb="Áreas", url_volver="/areas")