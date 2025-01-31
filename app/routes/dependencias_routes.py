from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
from app.controller.dependencias_controller import getAllDependencias, getDicValores, getPK, getCampos, postDependencias, deleteDependencia, getDependenciaById, updateDependencia

alcance_dependencias = Blueprint("dependencias", __name__)

@alcance_dependencias.route("/", methods=['GET'])
def dependencias():
    dic_valores = getDicValores()
    cabeceras = list(dic_valores.values())
    cabeceras.insert(0, "Acción")
    dependencias=getAllDependencias()
    pk=getPK()
    return render_template("leer.html", breadcrumb="Dependencias", valores=dependencias, dic_valores=dic_valores, cabeceras=cabeceras, pk=pk, url='dependencias')

@alcance_dependencias.route("/agregar", methods=['GET'])
def agregar():
    campos = getCampos()
    return render_template("agregarDependencia.html", breadcrumb="Dependencias", campos=campos, url='dependencias')

@alcance_dependencias.route("/agregar/nuevo", methods=["POST"])
def nuevo():
    crear = postDependencias(request.form)
    mensaje = crear['mensaje']
    estado = 'success' if crear['estado'] == 'éxito' else 'danger'
    flash(mensaje, estado)  # Guarda el mensaje en sesión flash

    return jsonify({
        "mensaje": mensaje,
        "estado": estado,
        "redirect": url_for('dependencias.dependencias')  # Devuelve la URL de redirección
    })

@alcance_dependencias.route("/eliminar/<int:id>", methods=['POST'])
def eliminar(id):
    eliminar = deleteDependencia(id)
    flash(eliminar['mensaje'], 'success' if eliminar['estado'] == 'éxito' else 'danger')
    return redirect(url_for('dependencias.dependencias'))

@alcance_dependencias.route("/editar/<int:id>", methods=['GET'])
def editar(id):
    dependencia = getDependenciaById(id)
    campos = getCampos()
    return render_template("editar.html", breadcrumb="Áreas", campos=campos, activo=dependencia, id=id, url='dependencias')

@alcance_dependencias.route("/actualizar/<int:id>", methods=['POST'])
def actualizar(id):
    actualizar = updateDependencia(request.form, id)
    flash(actualizar['mensaje'], 'success' if actualizar['estado'] == 'éxito' else 'danger')
    return redirect(url_for('dependencias.dependencias'))
