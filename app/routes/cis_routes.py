from flask import Blueprint, render_template, redirect, url_for, flash, request
from app.controller.cis_controller import getAllCis, getCampos, getDicValores, getPK, postCI, deleteCI, updateCI, getCiById

alcance_cis = Blueprint("cis", __name__)

@alcance_cis.route("/", methods=['GET'])
def cis():
    dic_valores = getDicValores()
    cabeceras = list(dic_valores.values())[:-3]
    cabeceras.insert(0, "Acción")
    cis = getAllCis()
    pk=getPK()
    return render_template("leer.html", breadcrumb="CI's", valores=cis, dic_valores=dic_valores, cabeceras=cabeceras, pk=pk, url='cis')

@alcance_cis.route("/agregar", methods=['GET'])
def agregar():
    campos = getCampos()
    return render_template("agregar.html", breadcrumb="CI's", campos=campos, url='cis')

@alcance_cis.route("/agregar/nuevo", methods=['POST'])
def nuevo():
    crear = postCI(request.form)
    flash(crear['mensaje'], 'success' if crear['estado'] == 'éxito' else 'danger')
    return redirect(url_for('cis.cis'))

@alcance_cis.route("/eliminar/<int:id>", methods=['POST'])
def eliminar(id):
    eliminar = deleteCI(id)
    flash(eliminar['mensaje'], 'success' if eliminar['estado'] == 'éxito' else 'danger')
    return redirect(url_for('cis.cis'))

@alcance_cis.route("/editar/<int:id>", methods=['GET'])
def editar(id):
    ci = getCiById(id)
    campos = getCampos()
    return render_template("editar.html", breadcrumb="CI's", campos=campos, ci=ci, id=id, url='cis')

@alcance_cis.route("/actualizar/<int:id>", methods=['POST'])
def actualizar(id):
    actualizar = updateCI(request.form, id)
    flash(actualizar['mensaje'], 'success' if actualizar['estado'] == 'éxito' else 'danger')
    return redirect(url_for('cis.cis'))
