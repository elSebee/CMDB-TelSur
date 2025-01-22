from flask import Blueprint, render_template, redirect, url_for, flash
from app.controller.servicios_controller import getAllServicios, getCampos

alcance_servicios = Blueprint("servicios", __name__)

@alcance_servicios.route("/", methods=['GET'])
def servicios():
    dic_valores = {
        "id_servicio": "ID",
        "alias": "Alias",
        "nomb_servicio": "Nombre", 
        "id_area_responsable": "Área Responsable", 
        "desc_servicio": "Descripción"
    }
    cabeceras = list(dic_valores.values())
    cabeceras.insert(0, "Acción")
    servicios = getAllServicios()
    return render_template("leer.html", breadcrumb="Servicios", valores=servicios, dic_valores=dic_valores, cabeceras=cabeceras, url_agregar=url_for('servicios.agregar'))

@alcance_servicios.route("/agregar", methods=['GET'])
def agregar():
    campos = getCampos()
    return render_template("agregar.html", breadcrumb="Servicios", campos=campos, url_volver=url_for('servicios.servicios'),  url_crear=url_for('servicios.nuevo'))

@alcance_servicios.route("/agregar/nuevo", methods=['POST'])
def nuevo():
    flash('Servicio creado correctamente!', 'success')
    return redirect(url_for('servicios.servicios'))