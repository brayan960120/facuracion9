from src.app import app
from flask import render_template
from flask_controller import FlaskController
from flask import session

class HomeController(FlaskController):
    @app.route('/')
    def index():
        if 'email' in session:
            return render_template('index.html', titulo_pagina = 'Inicio', email=session['email'])

        return render_template('formulario_login.html', titulo_pagina = 'Login')

   
 