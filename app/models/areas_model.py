from app.database.db import db

class Areas(db.Model):
    __tablename__ = 'PROCT_AREAS'

    id_area = db.Column(db.Integer, primary_key=True)
    desc_area = db.Column(db.String(200), nullable=False, unique=True)