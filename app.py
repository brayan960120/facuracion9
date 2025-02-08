from src.models import Base, engine
from flask_controller import FlaskControllerRegister
from flask_login import LoginManager
from src.models.usuarios import Usuarios
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)

app.secret_key = "mi llaveria"
app.debug = True

register = FlaskControllerRegister(app)
register.register_package('src.controllers')

Base.metadata.create_all(engine)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(id_usuario):
    return Usuarios.obtener_usuarios




if __name__ == '__main__':
    app.run(debug=True)




    


    