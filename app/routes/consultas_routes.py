from flask import Blueprint, render_template, redirect, url_for, flash, request
from app.controller.consultas_controller import getAllConsultas,  getDicValores, getPK, getCampos, postConsulta, deleteConsulta, getConsultaById, updateConsulta

alcance_consultas = Blueprint("consultas", __name__)

@alcance_consultas.route("/", methods=['GET'])
def consultas():
    dic_valores = getDicValores()
    cabeceras = list(dic_valores.values())
    cabeceras.insert(0, "Acción")
    consultas=getAllConsultas()
    pk=getPK()
    return render_template("leer.html", breadcrumb="Consultas", valores=consultas, dic_valores=dic_valores, cabeceras=cabeceras, pk=pk, url='consultas')

@alcance_consultas.route("/agregar", methods=['GET'])
def agregar():
    campos = getCampos()
    return render_template("agregar.html", breadcrumb="Consultas", campos=campos, url='consultas')

@alcance_consultas.route("/agregar/nuevo", methods=['POST'])
def nuevo():
    crear = postConsulta(request.form)
    flash(crear['mensaje'], 'success' if crear['estado'] == 'éxito' else 'danger')
    return redirect(url_for('consultas.consultas'))

@alcance_consultas.route("/eliminar/<int:id>", methods=['POST'])
def eliminar(id):
    eliminar = deleteConsulta(id)
    flash(eliminar['mensaje'], 'success' if eliminar['estado'] == 'éxito' else 'danger')
    return redirect(url_for('consultas.consultas'))

@alcance_consultas.route("/editar/<int:id>", methods=['GET'])
def editar(id):
    Consulta = getConsultaById(id)
    campos = getCampos()
    return render_template("editar.html", breadcrumb="Consultas", campos=campos, activo=Consulta, id=id, url='consultas')

@alcance_consultas.route("/actualizar/<int:id>", methods=['POST'])
def actualizar(id):
    actualizar = updateConsulta(request.form, id)
    flash(actualizar['mensaje'], 'success' if actualizar['estado'] == 'éxito' else 'danger')
    return redirect(url_for('consultas.consultas'))