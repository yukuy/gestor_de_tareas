#from flask import render_template, redirect, flash
from flask import render_template, redirect, flash, request, url_for, session
from app import app
from app.models.models import Usuario, db
from werkzeug.security import generate_password_hash, check_password_hash

#ruta para registrar 
@app.route("/register", methods=['GET', 'POST'])
def register():
    
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        clave = request.form['clave']
        
        clave_hash  = generate_password_hash(clave, method='pbkdf2:sha256', salt_length=8)
        
        nuevo_user = Usuario(nombre= nombre, correo=correo, clave=clave_hash)
        db.session.add(nuevo_user)
        db.session.commit()
        flash('El registro a sido exitoso')
        
        return redirect(url_for('login'))
    
    return render_template('register.html')

#ruta para login
@app.route("/", methods=['GET', 'POST'])
def login():
    
    if request.method == 'POST':
        correo = request.form['correo']
        clave = request.form['clave']
        
        #buscar usuario por correo
        usuario = Usuario.query.filter_by(correo=correo).first()
        if usuario and check_password_hash(usuario.clave, clave):
            session['user_id'] = usuario.id
            session['user_nombre'] = usuario.nombre
            session.permanent = True 
                
            return redirect(url_for('principal'))
        else:
            flash ('Correo o contraseña incorrecta', 'denger')
                
            
    return render_template("login.html")

@app.route("/principal")
def principal():
    if 'user_id' not in session:
        flash('por favor inicia secion primero', 'warning ')
        return redirect(url_for(login))
    
    usuario = Usuario.query.get(session['user_id'])
    
    return render_template("principal.html", user_nombre=session['user_nombre'], usuario=usuario)