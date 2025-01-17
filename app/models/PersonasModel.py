# from sqlalchemy import Column, String, Integer, ForeignKey
# from sqlalchemy.ext.declarative import declarative_base

# Base = declarative_base()

# class Persona(Base):
#     __tablename__ = 'PROCT_PERSONAS'

#     RUT = Column(String(15), primary_key=True, nullable=False)
#     nomb_persona = Column(String(50))
#     id_area = Column(Integer, ForeignKey('PROCT_AREAS.id_area'))
#     desc_gerencia = Column(String(100))
#     desc_cargo = Column(String(100))
#     mail = Column(String(50))
#     celular = Column(Integer)
#     codi_horario = Column(Integer)
#     mtdo_aviso_default = Column(String(20))