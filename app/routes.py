from flask import Blueprint, render_template, request

routes = Blueprint('routes', __name__)

# Página de inicio
@routes.route('/')
def index():
    mensaje = "Bienvenido al formulario de contacto"
    return render_template('index.html', mensaje=mensaje)

# Página de contacto
@routes.route('/contacto', methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        mensaje = request.form['mensaje']
        return render_template('gracias.html', nombre=nombre, correo=correo, mensaje=mensaje)
    return render_template('contacto.html')