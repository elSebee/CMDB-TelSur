from flask import Blueprint, render_template

alcance_global = Blueprint("menu", __name__)

@alcance_global.route("/", methods=['GET'])
def home():
    """Landing page route."""
    return render_template("index.html")