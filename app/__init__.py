from flask import Flask
from config import Config  # Ahora importamos correctamente la clase Config
from flask_sqlalchemy import SQLAlchemy

# Inicializar SQLAlchemy
db = SQLAlchemy()

# Crear la aplicación Flask
app = Flask(__name__)
app.config.from_object(Config)  # Usamos Config correctamente

# Inicializar SQLAlchemy con la aplicación
db.init_app(app)

# Importar rutas (asegúrate de que exista el módulo control_user)
from app.controls import control_user


