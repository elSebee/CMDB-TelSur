from flask import Blueprint, render_template

alcance_areas = Blueprint("areas", __name__)

@alcance_areas.route("/", methods=['GET'])
def areas():
    return render_template("areas.html")