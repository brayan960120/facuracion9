from src.app import app
from flask import render_template, request, redirect, url_for, flash
from flask_controller import FlaskController
from src.models.facturas import Facturas
from src.models.clientes import Clientes
from src.models.usuarios import Usuarios


class FacturasController(FlaskController):
    @app.route('/crear_factura', methods=['POST','GET'])
    def crear_factura():
        if request.method == 'POST':
            numero_factura = request.form.get('numero_factura')    
            fecha_factura = request.form.get('fecha_factura')
            cedula_cliente = request.form.get('cedula_cliente') 
            nombre_completo = request.form.get('nombre_completo') 
            direccion = request.form.get('direccion')    
            telefono = request.form.get('telefono')    
            email = request.form.get('email')         
            id_cliente = request.form.get('id_cliente')    
            id_usuario = request.form.get('id_usuario')
            if not numero_factura:
                flash('El numero de factura es un campo obligatorio')   
            elif not fecha_factura:
                flash('La fecha de la factura es un campo obligatorio')     
            elif not cedula_cliente:
                flash('El numero de cedula del cliente es un campo obligatorio')    
            elif not nombre_completo:
                flash('El nombre completo es un campo obligatorio')    
            elif not direccion:
                flash('La direccion es un campo obligatorio')
            elif not telefono:
                flash('El numero de telefono es un campo obligatorio')
            elif not email:
                flash('El email es un campo obligatorio')
            elif not id_cliente:
                flash('El id del cliente es un campo obligatorio') 
            elif not id_usuario:
                flash('El id del usuario es un campo obligatorio') 
            else:       
                factura = Facturas(numero_factura, fecha_factura, cedula_cliente, nombre_completo, direccion, telefono, email, id_cliente, id_usuario)
                Facturas.agregar_factura(factura)
                return redirect(url_for('ver_facturas'))
        
        usuarios = Usuarios.obtener_usuarios()
        return render_template('formulario_crear_factura.html', usuarios=usuarios, titulo_pagina = 'Crear Factura')
        

    @app.route('/ver_facturas')
    def ver_facturas():
        facturas = Facturas.obtener_facturas()
        return render_template('tabla_facturas.html', titulo_pagina = 'Ver Facturas', facturas=facturas)