from app import app, db
from app.models.models import Usuario  # IMPORTANTE: Importa el modelo antes de crear las tablas

# Crear las tablas
with app.app_context():
    db.create_all()
    print("✅ Tablas creadas con éxito.")

if __name__ == "__main__":
    app.run(debug=True)
