from flask import Blueprint, render_template, redirect, url_for, flash
from app.controller.cis_controller import getAllCis, getTiposDisponible

alcance_cis = Blueprint("cis", __name__)

@alcance_cis.route("/", methods=['GET'])
def cis():
    ids = ["Acción", "ID", "Alias", "Prioridad", "Tipo", "Estado", "Dirección IP", "Fecha", "URL", "Descripción"]
    cis = getAllCis()
    return render_template("leer.html", breadcrumb="CI's", valores=cis, ids=ids, url_agregar="/cis/agregar")

@alcance_cis.route("/agregar", methods=['GET'])
def cisAgregar():
    tipos = getTiposDisponible()
    return render_template("agregar.html", breadcrumb="CI's", url_volver="/cis", tipos=tipos)

@alcance_cis.route("/agregar/nuevo", methods=['POST'])
def cisNuevo():
    flash('CI creado correctamente!', 'success')
    return redirect(url_for('cis.cis'))