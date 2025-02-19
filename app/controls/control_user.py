#from flask import render_template, redirect, flash
from flask import render_template, redirect, flash, request, url_for, session
from app import app
from app.models.models import Usuario, db
from werkzeug.security import generate_password_hash, check_password_hash

def re(q, exp):
    if re.search(exp, q):
        return True
    return False

def es_clave_valided(clave):
    if len(clave) < 8:
        return "la Clave debe tener por minimo 8 caracteres."
    if not any (char.isupper() for char in clave):
        return "la Clave debe de incluir minusculas."
    if not any (char.islower()for char in clave):
        return "la Clave debe de incluir mayusculas."
    if not any (char.isdigit() for char in clave):
        return "la clave debe incluir numeros"
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", clave):
        return "La clave debe incluir al menos un símbolo especial (!@#$%^&*...)."
    return None


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

