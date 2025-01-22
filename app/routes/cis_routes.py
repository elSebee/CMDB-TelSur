from flask import Blueprint, render_template, redirect, url_for, flash
from app.controller.cis_controller import getAllCis, getCampos

alcance_cis = Blueprint("cis", __name__)

@alcance_cis.route("/", methods=['GET'])
def cis():
    dic_valores = {
        "id_ci": "ID",
        "alias": "Alias",
        "prioridad": "Prioridad", 
        "tipo_ci": "Tipo", 
        "estado": "Estado", 
        "dire_ip": "Dirección IP", 
        "fech_actualizacion": "Fecha", 
        "url": "URL", 
        "desc_ci": "Descripción"
    }
    cabeceras = list(dic_valores.values())[:-3]
    cabeceras.insert(0, "Acción")
    cis = getAllCis()
    return render_template("leer.html", breadcrumb="CI's", valores=cis, dic_valores=dic_valores, cabeceras=cabeceras, url_agregar=url_for('cis.agregar'))

@alcance_cis.route("/agregar", methods=['GET'])
def agregar():
    campos = getCampos()
    return render_template("agregar.html", breadcrumb="CI's", campos=campos, url_volver=url_for('cis.cis'), url_crear=url_for('cis.nuevo'))

@alcance_cis.route("/agregar/nuevo", methods=['POST'])
def nuevo():
    flash('CI creado correctamente!', 'success')
    return redirect(url_for('cis.cis'))