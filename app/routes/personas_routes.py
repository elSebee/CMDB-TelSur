from flask import Blueprint, render_template, redirect, url_for, flash, request
from app.controller.personas_controller import getAllPersonas, getCampos, getDicValores, getPK, postPersona, getPersonaById, deletePersona, updatePersona

alcance_personas = Blueprint("personas", __name__)

@alcance_personas.route("/", methods=['GET'])
def personas():
    dic_valores = getDicValores()
    cabeceras = list(dic_valores.values())
    cabeceras.insert(0, "Acción")
    personas = getAllPersonas()
    pk=getPK()
    return render_template("leer.html", breadcrumb="Personas", valores=personas, dic_valores=dic_valores, cabeceras=cabeceras, pk=pk, url='personas')

@alcance_personas.route("/agregar", methods=['GET'])
def agregar():
    campos = getCampos()
    return render_template("agregar.html", breadcrumb="Personas", campos=campos, url='personas')

@alcance_personas.route("/agregar/nuevo", methods=['POST'])
def nuevo():
    crear = postPersona(request.form)
    flash(crear['mensaje'], 'success' if crear['estado'] == 'éxito' else 'danger')
    return redirect(url_for('personas.personas'))

@alcance_personas.route("/eliminar/<string:id>", methods=['POST'])
def eliminar(id):
    eliminar = deletePersona(id)
    flash(eliminar['mensaje'], 'success' if eliminar['estado'] == 'éxito' else 'danger')
    return redirect(url_for('personas.personas'))

@alcance_personas.route("/editar/<string:id>", methods=['GET'])
def editar(id):
    persona = getPersonaById(id)
    campos = getCampos()
    return render_template("editar.html", breadcrumb="personas", campos=campos, activo=persona, id=id, url='personas')

@alcance_personas.route("/actualizar/<string:id>", methods=['POST'])
def actualizar(id):
    actualizar = updatePersona(request.form, id)
    flash(actualizar['mensaje'], 'success' if actualizar['estado'] == 'éxito' else 'danger')
    return redirect(url_for('personas.personas'))
