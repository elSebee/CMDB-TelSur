from flask import Blueprint, render_template, redirect, url_for, flash, request
from app.controller.servicios_controller import getAllServicios, getCampos, getDicValores, getPK, postServicio, deleteServicio, updateServicio, getServicioById

alcance_servicios = Blueprint("servicios", __name__)

@alcance_servicios.route("/", methods=['GET'])
def servicios():
    dic_valores = getDicValores()
    cabeceras = list(dic_valores.values())
    cabeceras.insert(0, "Acción")
    servicios = getAllServicios()
    pk=getPK()
    return render_template("leer.html", breadcrumb="Servicios", valores=servicios, dic_valores=dic_valores, cabeceras=cabeceras, pk=pk, url='servicios')

@alcance_servicios.route("/agregar", methods=['GET'])
def agregar():
    campos = getCampos()
    return render_template("agregar.html", breadcrumb="Servicios", campos=campos, url='servicios')

@alcance_servicios.route("/agregar/nuevo", methods=['POST'])
def nuevo():
    crear = postServicio(request.form)
    flash(crear['mensaje'], 'success' if crear['estado'] == 'éxito' else 'danger')
    return redirect(url_for('servicios.servicios'))

@alcance_servicios.route("/eliminar/<int:id>", methods=['POST'])
def eliminar(id):
    eliminar = deleteServicio(id)
    flash(eliminar['mensaje'], 'success' if eliminar['estado'] == 'éxito' else 'danger')
    return redirect(url_for('servicios.servicios'))

@alcance_servicios.route("/editar/<int:id>", methods=['GET'])
def editar(id):
    servicio = getServicioById(id)
    campos = getCampos()
    return render_template("editar.html", breadcrumb="Servicios", campos=campos, servicio=servicio, id=id, url='servicios')

@alcance_servicios.route("/actualizar/<int:id>", methods=['POST'])
def actualizar(id):
    actualizar = updateServicio(request.form, id)
    flash(actualizar['mensaje'], 'success' if actualizar['estado'] == 'éxito' else 'danger')
    return redirect(url_for('servicios.servicios'))
