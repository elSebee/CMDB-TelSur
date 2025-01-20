from flask import Blueprint, render_template
from app.models.servicios_model import Servicios
from app.database.db import db

alcance_servicios = Blueprint("servicios", __name__)

@alcance_servicios.route("/", methods=['GET'])
def servicios():
    servicios = Servicios.query.all()
    return render_template("servicios.html", servicios=servicios)