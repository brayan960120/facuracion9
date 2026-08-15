from itsdangerous import URLSafeTimedSerializer
from flask_mail import Mail, Message
from src.app import app
from flask import render_template, request, redirect, url_for,session, flash
from flask_controller import FlaskController
from src.models.usuarios import Usuarios
from flask_login import login_user
from src.mail import mail
from flask_mail import Message
from src.models import session as db_session

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
        
        
def generar_token(email):

    serializer = URLSafeTimedSerializer(app.secret_key)

    token = serializer.dumps(
        email,
        salt="recuperar-password"
    )

    return token

@app.route("/olvidar-password", methods=["GET", "POST"])
def olvidar_password():

    if request.method == "POST":

        email = request.form.get("email")

        usuario = Usuarios.email_existe(email)

        if usuario:

            token = generar_token(email)

            enlace = url_for(
                "restablecer_password",
                token=token,
                _external=True
            )

            mensaje = Message(
                subject="Recuperar contraseña - Inventtools",
                sender=app.config["MAIL_USERNAME"],
                recipients=[email]
            )

            mensaje.body = f"""
Hola {usuario.nombre_completo}.

Recibimos una solicitud para cambiar tu contraseña.

Haz clic en el siguiente enlace:

{enlace}

Este enlace es válido durante 1 hora.

Si tú no solicitaste este cambio, ignora este correo.
"""

            mail.send(mensaje)

        flash(
            "Si el correo está registrado, recibirás un enlace."
        )

        return redirect(url_for("login"))

    return render_template(
        "olvidar_password.html",
        titulo_pagina="Recuperar contraseña"
    )

@app.route(
    "/restablecer-password/<token>",
    methods=["GET", "POST"]
)
def restablecer_password(token):

    serializer = URLSafeTimedSerializer(app.secret_key)

    try:

        email = serializer.loads(
            token,
            salt="recuperar-password",
            max_age=3600
        )

    except Exception:

        flash("El enlace es inválido o ha expirado.")

        return redirect(url_for("login"))

    usuario = Usuarios.email_existe(email)

    if not usuario:

        flash("Usuario no encontrado.")

        return redirect(url_for("login"))

    if request.method == "POST":

        password = request.form.get("password")
        confirmar_password = request.form.get(
            "confirmar_password"
        )

        if password != confirmar_password:

            flash("Las contraseñas no coinciden.")

            return render_template(
                "restablecer_password.html"
            )

        # Guardamos directamente la contraseña
        usuario.contraseña = password

        db_session.commit()

        flash("Contraseña actualizada correctamente.")

        return redirect(url_for("login"))

    return render_template(
        "restablecer_password.html"
    )

@app.route('/logout')
def logout():
    session.pop('email', None)  # Cerrar sesión
    flash('Has salido exitosamente.')
    return redirect(url_for('login'))

