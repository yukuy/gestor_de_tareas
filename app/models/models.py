from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from app import db

#modelo de usuarios 
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(200), nullable=False)    
    clave = db.Column(db.String(200), nullable=False)
    
     # Relación con Tareas (un usuario puede tener muchas tareas)
    tareas = db.relationship('Tareas', backref='responsable', lazy=True, cascade="all, delete-orphan")

    
#MODELO DE LA TABLA TAREAS
class Tareas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(500), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    fecha_creacion = db.Column(db.Date, default=datetime.utcnow, nullable=False)
    fecha_limite = db.Column(db.Date, nullable=True)
    prioridad = db.Column(db.Enum('baja', 'media', 'alta', name='prioridad_enum'), default='media')
    estado = db.Column(db.Enum('pendiente', 'progreso', 'completada', name='estado_enum'), default='pendiente')

    # Clave foránea con ondelete="SET NULL"
    responsable_id = db.Column(db.Integer, db.ForeignKey('usuario.id', ondelete="CASCADE"), nullable=False)