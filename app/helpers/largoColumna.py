from sqlalchemy.sql.sqltypes import String

def find_large_string_columns(model):
    """
    Encuentra columnas con tipo String y longitud mayor a 100 en un modelo SQLAlchemy.
    :param model: Clase del modelo SQLAlchemy.
    :return: Lista de columnas con longitud > 100.
    """
    large_string_columns = []
    
    for column in model.__table__.columns:
        # Verifica si la columna es del tipo String y tiene un límite mayor a 100
        if isinstance(column.type, String) and column.type.length and column.type.length > 100:
            large_string_columns.append({
                'name': column.name,
                'max_length': column.type.length
            })
    return large_string_columns
