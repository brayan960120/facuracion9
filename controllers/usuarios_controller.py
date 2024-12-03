from src.app import app
from flask import render_template, request, redirect, url_for, flash
from flask_controller import FlaskController
from src.models.usuarios import Usuarios


class UsuariosController(FlaskController):
    @app.route('/crear_usuario', methods=['POST','GET'])
    def crear_usuario():
        if request.method == 'POST':
            nombre_completo = request.form.get('nombre_completo')    
            email = request.form.get('email')    
            contraseña = request.form.get('contraseña')    
            rol = request.form.get('rol')  
            if not nombre_completo:
                flash('El nombre completo es un campo obligatorio')   
            elif not email:
                flash('El email es un campo obligatorio')     
            elif not contraseña:
                flash('La contraseña es un campo obligatorio')    
            elif not rol:
                flash('El rol en stock es un campo obligatorio')     
            else:    
                    usuario = Usuarios(nombre_completo, email, contraseña, rol)
                    Usuarios.agregar_usuario(usuario)
                    return redirect(url_for('ver_usuarios'))
        return render_template('formulario_crear_usuario.html', titulo_pagina = 'Crear Usuario')

    @app.route('/ver_usuarios')
    def ver_usuarios():
        usuarios = Usuarios.obtener_usuarios()
        return render_template('tabla_usuarios.html', titulo_pagina = 'Ver Usuarios', usuarios= usuarios)
    
    
    @app.route('/eliminar_usuario/<id>')
    def eliminar_usuario(id):
        Usuarios.eliminar_usuario(id)
        usuarios = Usuarios.obtener_usuarios()
        return render_template('tabla_usuarios.html', titulo_pagina = 'Ver Usuarios', usuarios=usuarios)
    

    @app.route('/actualizar_usuario/<id>', methods=['GET', 'POST'])
    def actualizar_usuario(id):
        if request.method == 'GET':
        # Lógica para mostrar el formulario de edición con los datos actuales del producto
            usuario= Usuarios.obtener_usuario_por_id(id)
            return render_template('formulario_actualizar_usuario.html',titulo_pagina = 'Actualizar Usuario', usuario=usuario)

        if request.method == 'POST':
        # Lógica para procesar la actualización del 
            id_usuario = request.form.get('id')    
            nombre_completo = request.form.get('nombre_completo')    
            email = request.form.get('email')    
            contraseña = request.form.get('contraseña') 
            rol = request.form.get('rol')   

        # Actualizar el producto en la base de datos
            usuario_modificar = Usuarios(nombre_completo,email,contraseña,rol)
            Usuarios.actualizar_usuario(usuario_modificar,id_usuario)
            
            
            return redirect(url_for('ver_usuarios'))