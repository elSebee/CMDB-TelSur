from flask import Blueprint, render_template
from app.models.servicios_model import Servicios
from app.database.db import db

alcance_servicios = Blueprint("servicios", __name__)

@alcance_servicios.route("/", methods=['GET'])
def servicios():
    ids = ["Acción", "ID", "Alias", "Nombre", "Área Responsable", "Descripción"]
    servicios = Servicios.query.all()
    return render_template("leer.html", breadcrumb="Servicios", valores=servicios, ids=ids, url_agregar="/servicios/agregar")

@alcance_servicios.route("/agregar", methods=['GET'])
def serviciosAgregar():
    return render_template("agregar.html", breadcrumb="Servicios", url_volver="/servicios")