from src.app import app
from flask import render_template, request, redirect, url_for, flash
from flask_controller import FlaskController
from src.models.clientes import Clientes
from flask import session
from src.models.facturas import Facturas

class ClientesController(FlaskController):
    @app.route('/crear_cliente', methods=['POST','GET'])
    def crear_cliente():
        if 'email' in session:
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
                elif Clientes.email_existe(email):
                    flash('El email ya existe')

                else:     
                    cliente = Clientes(numero_identificacion, nombre_completo, direccion, telefono, email)
                    Clientes.agregar_cliente(cliente)
                    return redirect(url_for('ver_clientes'))
            return render_template('formulario_crear_cliente.html', titulo_pagina = 'Crear Cliente')
        return render_template('formulario_login.html', titulo_pagina = 'Login')

    
    @app.route('/ver_clientes')
    def ver_clientes():
        if 'email' in session:
            clientes = Clientes.obtener_clientes()
            return render_template('tabla_clientes.html', titulo_pagina = 'ver clientes', clientes = clientes)
        return render_template('formulario_login.html', titulo_pagina = 'Login')
        
    

    @app.route('/consultar_cliente_numero_identificacion/<numero_identificacion>')
    def consultar_cliente_numero_identificacion(numero_identificacion):
        cliente = Clientes.obtener_cliente_por_numero_identificacion(numero_identificacion)
        return cliente 

    
    @app.route('/eliminar_clientes/<id>')
    def eliminar_cliente(id):
        if Facturas.obtener_facturas_por_cliente(id):
            flash('No se puede eliminar el cliente porque tiene facturas asociadas')
            clientes = Clientes.obtener_clientes()
            return render_template('tabla_clientes.html', titulo_pagina= 'Ver clientes', clientes=clientes)
        else:
            Clientes.eliminar_cliente(id)
            clientes = Clientes.obtener_clientes()
            return render_template('tabla_clientes.html', titulo_pagina='Ver clientes', clientes=clientes)
    
    
    @app.route('/actualizar_cliente/<id>', methods=['GET', 'POST'])
    def actualizar_cliente(id):
        if 'email' in session:
            if request.method == 'GET':
        # Lógica para mostrar el formulario de edición con los datos actuales del producto
                cliente= Clientes.obtener_cliente_por_id(id)
                return render_template('formulario_actualizar_cliente.html',titulo_pagina = 'Actualizar Cliente', cliente = cliente)

            if request.method == 'POST':
        # Lógica para procesar la actualización del 
                id_cliente = request.form.get('id')    
                numero_identificacion = request.form.get('numero_identificacion')    
                nombre_completo = request.form.get('nombre_completo')    
                direccion = request.form.get('direccion')    
                telefono  = request.form.get('telefono')    
                email = request.form.get('email')

        # Actualizar el producto en la base de datos
                cliente_modificar = Clientes(numero_identificacion,nombre_completo,direccion,telefono,email)
                Clientes.actualizar_cliente(cliente_modificar,id_cliente)
                return redirect(url_for('ver_clientes'))
        return render_template('formulario_login.html', titulo_pagina = 'Login')
  