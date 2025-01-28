from flask import Flask
from config import config
from flask_sqlalchemy import SQLAlquemy


#inicializar  sqlalchemy
db = SQLAlquemy()

#crear la aplicacion flask 
app = Flask(__name__)
app.config.from_obgect(config)

#ibnicializar sqlalchemy con la aplaicacion 
db.init_app(app)

#importar rutas
from app.controls import ruta1 
