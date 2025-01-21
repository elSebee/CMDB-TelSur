from flask import Blueprint, render_template

alcance_personas = Blueprint("personas", __name__)

@alcance_personas.route("/", methods=['GET'])
def personas():
    ids = ["Acción", "R.U.T", "Nombre", "Área", "Cargo", "Mail", "Teléfono", "Método Aviso"]
    personas = []
    return render_template("leer.html", breadcrumb="Personas", valores=personas, ids=ids, url_agregar="/personas/agregar")

@alcance_personas.route("/agregar", methods=['GET'])
def personasAgregar():
    return render_template("agregar.html", breadcrumb="Personas", url_volver="/personas")