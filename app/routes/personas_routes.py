from flask import Blueprint, render_template, redirect, url_for, flash
from app.controller.personas_controller import getAllPersonas, getCampos

alcance_personas = Blueprint("personas", __name__)

@alcance_personas.route("/", methods=['GET'])
def personas():
    ids = ["Acción", "R.U.T", "Nombre", "Área", "Cargo", "Mail", "Teléfono", "Método Aviso"]
    personas = getAllPersonas()
    return render_template("leer.html", breadcrumb="Personas", valores=personas, ids=ids, url_agregar=url_for('personas.agregar'))

@alcance_personas.route("/agregar", methods=['GET'])
def agregar():
    campos = getCampos()
    return render_template("agregar.html", breadcrumb="Personas", campos=campos, url_volver=url_for('personas.personas'), url_crear=url_for('personas.nuevo'))

@alcance_personas.route("/agregar/nuevo", methods=['POST'])
def nuevo():
    flash('Persona creada correctamente!', 'success')
    return redirect(url_for('personas.personas'))