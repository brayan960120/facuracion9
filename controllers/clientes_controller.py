from src.app import app
from flask import render_template, request, redirect, url_for, flash
from flask_controller import FlaskController
from src.models.clientes import Clientes

class ClientesController(FlaskController):
    @app.route('/crear_cliente', methods=['POST','GET'])
    def crear_cliente():
        if request.method == 'POST':
            numero_identificacion = request.form.get('numero_identificacion')    
            nombre_completo = request.form.get('nombre_completo')    
            direccion = request.form.get('direccion')
            telefono = request.form.get('telefono') 
            email =  request.form.get('email')
            if not numero_identificacion:
                flash('El numero de identificacion es un campo obligatorio')   
            elif not nombre_completo:
                flash('El nombre completo es un campo obligatorio')     
            elif not direccion:
                flash('La direccion es un campo obligatorio')    
            elif not telefono:
                flash('El telefono es un campo obligatorio')    
            elif not email:
                flash('El email es un campo obligatorio')  
            else:     
                cliente = Clientes(numero_identificacion, nombre_completo, direccion, telefono, email)
                Clientes.agregar_cliente(cliente)
                return redirect(url_for('ver_clientes'))
        return render_template('formulario_crear_cliente.html', titulo_pagina = 'Crear Cliente')

    
    @app.route('/ver_clientes')
    def ver_clientes():
        clientes = Clientes.obtener_clientes()
        return render_template('tabla_clientes.html', titulo_pagina = 'ver clientes', clientes = clientes)
    

    @app.route('/consultar_cliente_numero_identificacion/<numero_identificacion>')
    def consultar_cliente_numero_identificacion(numero_identificacion):
        cliente = Clientes.obtener_cliente_por_numero_identificacion(numero_identificacion)
        return cliente 

    
    @app.route('/eliminar_clientes/<id>')
    def eliminar_cliente(id):
        Clientes.eliminar_cliente(id)
        clientes = Clientes.obtener_clientes()
        return render_template('tabla_clientes.html', titulo_pagina = 'ver clientes', clientes = clientes)
  