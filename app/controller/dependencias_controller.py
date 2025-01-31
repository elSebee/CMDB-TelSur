from app.models import Dependencias, Servicios, CMDBConfItems
from app.database.db import db
from sqlalchemy.orm import aliased
from app.controller.servicios_controller import getAllServicios
from app.controller.cis_controller import getAllCis

class DependenciasNames:
    def __init__(self, id_relacion, alias_ci_origen, alias_ci_destino, alias_servicio, tipo_relacion):
        self.id_relacion = id_relacion
        self.alias_ci_origen = alias_ci_origen
        self.alias_ci_destino = alias_ci_destino
        self.alias_servicio = alias_servicio
        self.tipo_relacion = tipo_relacion

def getAllDependencias():
    ci_origen = aliased(CMDBConfItems, name='id_ci_origen')
    ci_destino = aliased(CMDBConfItems, name='id_ci_destino')

    dependencias = (
        db.session.query(
            Dependencias.id_relacion,
            ci_origen.alias.label('alias_ci_origen'),
            ci_destino.alias.label('alias_ci_destino'),
            Servicios.alias.label('alias_servicio'),
            Dependencias.tipo_relacion
        )
        .join(ci_origen, ci_origen.id_ci == Dependencias.id_ci_origen)
        .join(ci_destino, ci_destino.id_ci == Dependencias.id_ci_destino)
        .join(Servicios, Servicios.id_servicio == Dependencias.id_servicio)
    ).all()

    return [DependenciasNames(*row) for row in dependencias]



def getDependenciaById(id):
    dependencia = Dependencias.query.get_or_404(id)
    return dependencia

def getCampos():
    cis = getAllCis()
    opciones_ci = {ci.id_ci: ci.alias for ci in cis}
    servicios = getAllServicios()
    opciones_servicio = {servicio.id_servicio: servicio.alias for servicio in servicios}
    opciones_relacion = {
        'Depende de': 'Depende de',
        'Hospedado en': 'Hospedado en',
        'Conectado a': 'Conectado a',
        'Impacta': 'Impacta',
        'Pertenece a': 'Pertenece a'
    }
    campos = [
        {"name": "id_ci_origen", "type": "select", "label": "CI Origen", "options": opciones_ci, "required": True},
        {"name": "tipo_relacion", "type": "select", "label": "Relación", "options": opciones_relacion, "required": True},
        {"name": "id_ci_destino", "type": "select", "label": "CI Destino", "options": opciones_ci, "required": True},
        {"name": "id_servicio", "type": "select", "label": "ID Servicio", "options": opciones_servicio, "required": True}
    ]
    return campos

def getDicValores():
    return {
        "id_relacion": "ID",
        "alias_ci_origen": "CI Origen",
        "alias_ci_destino": "CI Destino",
        "alias_servicio": "ID Servicio",
        "tipo_relacion": "Descripción Relación"
    }

def getPK():
    dependencia = Dependencias(
        id_ci_origen=1,
        id_ci_destino=2,
        id_servicio=3,
        tipo_relacion="Relacion temporal"
    )

    return dependencia.pk_name

def postDependencias(form):
    dependencias = {}

    # Recorrer el ImmutableMultiDict
    for key, value in form.items():
        if "[" in key and "]" in key:  # Solo procesar campos indexados
            # Extraer el nombre del campo y el índice
            field_name, index = key.split("[")
            index = index.strip("]")

            # Crear un diccionario para el índice si no existe
            if index not in dependencias:
                dependencias[index] = {}

            # Agregar el valor al diccionario correspondiente
            dependencias[index][field_name] = value

    # Convertir el diccionario a una lista de objetos
    result = list(dependencias.values())

    print(result)

    for dependencia in result:

        id_ci_origen = dependencia['id_ci_origen']
        id_ci_destino = dependencia['id_ci_destino']
        id_servicio = dependencia['id_servicio']
        tipo_relacion = dependencia['tipo_relacion']
        try:
            new_dependencia = Dependencias(
                id_ci_origen=id_ci_origen,
                id_ci_destino=id_ci_destino,
                id_servicio=id_servicio,
                tipo_relacion=tipo_relacion
            )
            db.session.add(new_dependencia)
            db.session.commit()

        except Exception as e:
            db.session.rollback()
            return {
                "estado": "error",
                "mensaje": f"¡Error al crear una Dependencia: {str(e)}!"
            }
        
    return {
        "estado": "éxito",
        "mensaje": "¡Dependencias creadas con éxito!",
    }

def deleteDependencia(id):
    try:
        dependencia = getDependenciaById(id)  # Si no existe, lanza un error 404

        db.session.delete(dependencia)
        db.session.commit()

        return {
            "estado": "éxito",
            "mensaje": "¡Dependencia eliminada con éxito!",
        }
    except Exception as e:
        db.session.rollback()
        return {
            "estado": "error",
            "mensaje": f"¡Error al eliminar el Dependencia: {str(e)}!"
        }
    
def updateDependencia(form, id_dependencia):
    id_ci_origen = form.get('id_ci_origen')
    id_ci_destino = form.get('id_ci_destino')
    id_servicio = form.get('id_servicio')
    tipo_relacion = form.get('tipo_relacion')

    try:
        depen_a_actualizar = getDependenciaById(id_dependencia)
        if not depen_a_actualizar:
            return {
                "estado": "error",
                "mensaje": "¡Dependencia no encontrado!"
            }

        # Actualiza los campos del registro
        depen_a_actualizar.id_ci_origen = id_ci_origen
        depen_a_actualizar.id_ci_destino = id_ci_destino
        depen_a_actualizar.id_servicio = id_servicio
        depen_a_actualizar.tipo_relacion = tipo_relacion

        # Guarda los cambios en la base de datos
        db.session.commit()

        return {
            "estado": "éxito",
            "mensaje": "¡Dependencia actualizada con éxito!"
        }

    except Exception as e:
        db.session.rollback()
        return {
            "estado": "error",
            "mensaje": f"¡Error al actualizar el Dependencia: {str(e)}!"
        }