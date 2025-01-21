from flask import Blueprint, render_template, redirect, url_for, flash
from app.controller.areas_controller import getAllAreas, getCampos


alcance_areas = Blueprint("areas", __name__)

@alcance_areas.route("/", methods=['GET'])
def areas():
    ids = ["Acción", "ID", "Nombre", "Empresa", "Descripción"]
    areas=getAllAreas()
    return render_template("leer.html", breadcrumb="Áreas", valores=areas, ids=ids, url_agregar=url_for('areas.agregar'))

@alcance_areas.route("/agregar", methods=['GET'])
def agregar():
    campos = getCampos()
    return render_template("agregar.html", breadcrumb="Áreas", campos=campos, url_volver=url_for('areas.areas'), url_crear=url_for('areas.nuevo'))

@alcance_areas.route("/agregar/nuevo", methods=['POST'])
def nuevo():
    flash('Área creada correctamente!', 'success')
    return redirect(url_for('areas.areas'))