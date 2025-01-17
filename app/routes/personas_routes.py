from flask import Blueprint, render_template

alcance_personas = Blueprint("personas", __name__)

@alcance_personas.route("/", methods=['GET'])
def personas():
    return render_template("personas.html")