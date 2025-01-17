from flask import Blueprint, render_template

alcance_servicios = Blueprint("servicios", __name__)

@alcance_servicios.route("/", methods=['GET'])
def servicios():
    return render_template("servicios.html")