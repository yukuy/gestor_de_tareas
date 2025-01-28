from app import app, db
import os 

#crear tablas en la bd
with app.app_context():
    db.create_all() #crear las tablas al iniciar la aplicacion 
    print ("tablas creadas con exito")

if __name__ == "__main__":
    app.run(debug=True)
