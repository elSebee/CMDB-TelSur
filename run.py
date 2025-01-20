from app import app
from app.database.db import db

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run()