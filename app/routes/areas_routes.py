from flask import Blueprint, render_template, redirect, url_for, flash, request
from app.controller.areas_controller import getAllAreas, getCampos, getDicValores, postArea, getPK, deleteArea, updateArea, getAreaById

alcance_areas = Blueprint("areas", __name__)

@alcance_areas.route("/", methods=['GET'])
def areas():
    dic_valores = getDicValores()
    cabeceras = list(dic_valores.values())
    cabeceras.insert(0, "Acción")
    areas=getAllAreas()
    pk=getPK()
    return render_template("leer.html", breadcrumb="Áreas", valores=areas, dic_valores=dic_valores, cabeceras=cabeceras, pk=pk, url='areas')

@alcance_areas.route("/agregar", methods=['GET'])
def agregar():
    campos = getCampos()
    return render_template("agregar.html", breadcrumb="Áreas", campos=campos, url='areas')

@alcance_areas.route("/agregar/nuevo", methods=['POST'])
def nuevo():
    crear = postArea(request.form)
    flash(crear['mensaje'], 'success' if crear['estado'] == 'éxito' else 'danger')
    return redirect(url_for('areas.areas'))

@alcance_areas.route("/eliminar/<int:id>", methods=['POST'])
def eliminar(id):
    eliminar = deleteArea(id)
    flash(eliminar['mensaje'], 'success' if eliminar['estado'] == 'éxito' else 'danger')
    return redirect(url_for('areas.areas'))

@alcance_areas.route("/editar/<int:id>", methods=['GET'])
def editar(id):
    area = getAreaById(id)
    campos = getCampos()
    return render_template("editar.html", breadcrumb="Áreas", campos=campos, area=area, id=id, url='areas')

@alcance_areas.route("/actualizar/<int:id>", methods=['POST'])
def actualizar(id):
    actualizar = updateArea(request.form, id)
    flash(actualizar['mensaje'], 'success' if actualizar['estado'] == 'éxito' else 'danger')
    return redirect(url_for('areas.areas'))
