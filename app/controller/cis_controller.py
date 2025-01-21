from app.models.cis_model import CMDBConfItems

def getAllCis():
    return CMDBConfItems.query.all()

def getTiposDisponible():
    return ['Servidor', 'Aplicación', 'Base de Datos', 'Web Service', 'Listener DB', 'Esquema', 'Sitio Web', 'Vista', 'Otros']