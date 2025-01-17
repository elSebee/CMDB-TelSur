from flask import Blueprint, render_template

alcance_cis = Blueprint("cis", __name__)

@alcance_cis.route("/", methods=['GET'])
def cis():
    return render_template("cis.html")