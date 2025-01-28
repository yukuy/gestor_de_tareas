import secrets 
from datetime import timedelta

#conexion a la base de datos en supabase
class config:
    #base de datos de postgresql
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:[YOUR-PASSWORD]@db.ykausbwiigwodbcpdtdc.supabase.co:5432/postgres'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'tu_clave_secreta_fija_aqui'  
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)