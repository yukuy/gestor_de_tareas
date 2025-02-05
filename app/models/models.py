from werkzeug.security import generate_password_hash, check_password_hash
from app import db

#modelo de usuarios 
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(200), nullable=False)    
    clave = db.Column(db.String(200), nullable=False)
    
    
    