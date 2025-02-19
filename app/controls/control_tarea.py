from flask import render_template, redirect, request, url_for, session, flash
from app import app
from app.models.models import Tareas, Usuario, db
import datetime

# Ruta para agregar nuevas tareas 
@app.route('/add_task', methods=['GET', 'POST'])
def add_task():
    
    if 'user_id' not in session:
        flash('Debes iniciar sesión para agregar una tarea.', 'warning')
        return redirect(url_for('login'))
    
    # Recepción de los valores desde el formulario
    if request.method == 'POST':
        print ("solicitud POST recivida:")
        
        titulo = request.form.get('titulo')  # Corregido
        descripcion = request.form.get('descripcion')
        fecha_creacion = request.form.get('fecha_creacion')
        fecha_limite = request.form.get('fecha_limite')
        prioridad = request.form.get('prioridad')
        
        responsable_id = session.get('user_id')  # Corregido para evitar error si no hay sesión
        
        print("datos recividos", titulo, descripcion)
        
        # Convertir fechas correctamente
        fecha_creacion = datetime.datetime.strptime(fecha_creacion, '%Y-%m-%d').date()
        fecha_limite = datetime.datetime.strptime(fecha_limite, '%Y-%m-%d').date()

        #dejar el estado por defecto al crar las tareas 
        estado = "pendiente"
        # Crear el registro en la base de datos
        nueva_tarea = Tareas(
            titulo=titulo, 
            descripcion=descripcion, 
            fecha_creacion=fecha_creacion, 
            fecha_limite=fecha_limite,
            prioridad=prioridad, 
            estado=estado, 
            responsable_id=responsable_id
        )
        
        db.session.add(nueva_tarea)
        db.session.commit()
        
        flash('Tarea creada con éxito', 'success')
        return redirect(url_for('principal'))

    return render_template('add_task.html')

#ruta para editar el estado
@app.route("/edit_task/edit<int:id>", methods=['GET', 'POST'])
def edit_task(id):
    tareas = Tareas.query.get_or_404(id)
    
    return render_template('edit_task.html')

    

#mostar las tareas 
@app.route("/principal")
def principal():
    if 'user_id' not in session:
        flash('por favor inicia secion primero', 'warning ')
        return redirect(url_for('login'))
    
    #obtengo el usuario de la session 
    usuario = Usuario.query.get(session['user_id'])
    
    #obtener las tareas por el usario que inicio sesion 
    tasks = Tareas.query.filter_by(responsable_id=usuario.id).all()
    
    
    return render_template("principal.html", user_nombre=session['user_nombre'], usuario=usuario, tasks=tasks)

