from flask import Flask, request
from config import Config
# from .database.contact_db import reset_table

from .routes import alcance_global, alcance_servicios, alcance_cis, alcance_dependencias, alcance_personas, alcance_areas

app = Flask(__name__, static_folder=Config.STATIC_FOLDER, template_folder=Config.TEMPLATE_FOLDER)
app.config.from_object(Config)

@app.context_processor
def inject_request():
    return dict(request=request)

app.register_blueprint(alcance_global, url_prefix="/")
app.register_blueprint(alcance_servicios, url_prefix="/servicios")
app.register_blueprint(alcance_cis, url_prefix="/cis")
app.register_blueprint(alcance_dependencias, url_prefix="/dependencias")
app.register_blueprint(alcance_areas, url_prefix="/areas")
app.register_blueprint(alcance_personas, url_prefix="/personas")

# reset_table()