from flask import Blueprint, render_template

alcance_dependencias = Blueprint("dependencias", __name__)

@alcance_dependencias.route("/", methods=['GET'])
def dependencias():
    return render_template("dependencias.html")