import sqlite3

def verificar_tablas():
    conexion = sqlite3.connect("Gestor_de_tareas.db")  # Asegúrate de que el nombre del archivo es correcto
    cursor = conexion.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tablas = cursor.fetchall()

    print("Tablas en la base de datos:", tablas)

    conexion.close()

verificar_tablas()
