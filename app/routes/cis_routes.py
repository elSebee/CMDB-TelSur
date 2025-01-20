from flask import Blueprint, render_template
from app.models.cis_model import CMDBConfItems
from app.database.db import db

alcance_cis = Blueprint("cis", __name__)

@alcance_cis.route("/", methods=['GET'])
def cis():
    cis = CMDBConfItems.query.all()
    return render_template("cis.html", cis=cis)