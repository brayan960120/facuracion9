from src.app import app
from flask import render_template, request, redirect, url_for,session, flash
from flask_controller import FlaskController
from src.models.usuarios import Usuarios
from flask_login import login_user

class LoginController(FlaskController):
    @app.route('/login', methods=['POST','GET'])
    def login():    
        if request.method == 'POST':
            email = request.form.get('email')                
            contraseña = request.form.get('contrasena')    
            usuario_valido = Usuarios.validar_usuario(email, contraseña)
            if usuario_valido:
                session['email']= email
                flash('Has iniciado sesion exitosamente')
                return redirect(url_for('index'))
            else:
                flash('El email o la contraseña son incorrectos')
        return render_template('formulario_login.html', titulo_pagina = 'login')
        
        


@app.route('/logout')
def logout():
    session.pop('email', None)  # Cerrar sesión
    flash('Has salido exitosamente.')
    return redirect(url_for('login'))

