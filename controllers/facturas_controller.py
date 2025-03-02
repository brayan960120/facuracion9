from src.app import app
from flask import render_template, request, redirect, url_for, flash
from flask_controller import FlaskController
from src.models.facturas import Facturas
from src.models.clientes import Clientes
from src.models.usuarios import Usuarios
from src.models.productos import Productos
from src.models.detalle_facturas import DetalleFacturas
from flask import session


class FacturasController(FlaskController):
    @app.route('/crear_factura/<id>', methods=['POST','GET'])
    def crear_factura_por(id):
        if 'email' in session:
            if request.method == 'POST':
                numero_factura = request.form.get('numero_factura')    
                fecha_factura = request.form.get('fecha_factura')
                cedula_cliente = request.form.get('cedula_cliente') 
                nombre_completo = request.form.get('nombre_completo') 
                direccion = request.form.get('direccion')    
                telefono = request.form.get('telefono')    
                email = request.form.get('email')    
                valor_total = request.form.get('valor_total')
                id_cliente = request.form.get('id_cliente')    
                id_usuario = request.form.get('id_usuario')
                id_detalle_factura = request.form.get('id_detalle_factura')
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
                    factura = Facturas(numero_factura, fecha_factura, cedula_cliente, nombre_completo, direccion, telefono, email, valor_total, id_cliente, id_usuario,id_detalle_factura)
                    Facturas.agregar_factura(factura)
                    return redirect(url_for('ver_facturas'))
                
            
            detalle_facturas = DetalleFacturas.obtener_detalle_facturas_por_id(id)
            usuarios = Usuarios.obtener_usuarios()  
            producto = Productos.obtener_productos()
            clientes = Clientes.obtener_clientes()
            
            return render_template('formulario_crear_factura.html', usuarios=usuarios,producto=producto,detalle_facturas=detalle_facturas,clientes=clientes,titulo_pagina = 'Crear Factura')
        return render_template('formulario_login.html', titulo_pagina = 'Login')
    

    @app.route('/ver_facturas')
    def ver_facturas():
        if 'email' in session:
            facturas = Facturas.obtener_facturas()
            return render_template('tabla_facturas.html', titulo_pagina = 'Ver Facturas', facturas=facturas)
        return render_template('formulario_login.html', titulo_pagina = 'Login')
        
    
    @app.route('/eliminar_facturas/<id>')
    def eliminar_factura(id):
        Facturas.eliminar_factura(id)
        facturas = Facturas.obtener_facturas()
        return render_template('tabla_facturas.html', titulo_pagina = 'Ver facturas', facturas = facturas)
    
    @app.route('/actualizar_factura/<id>', methods=['GET', 'POST'])
    def actualizar_factura(id):
        if 'email' in session:
        
            if request.method == 'GET':
        # Lógica para mostrar el formulario de edición con los datos actuales del producto
                detalle_facturas = DetalleFacturas.obtener_detalle_facturas()
                factura = Facturas.obtener_factura_por_id(id)
                cliente = Clientes.obtener_clientes()
                usuario = Usuarios.obtener_usuarios()
                
                return render_template('formulario_actualizar_factura.html',titulo_pagina = 'Actualizar Facturas', factura = factura , cliente = cliente, usuario = usuario, detalle_facturas=detalle_facturas)

            if request.method == 'POST':
        # Lógica para procesar la actualización del 
                id_factura = request.form.get('id')    
                numero_factura = request.form.get('numero_factura')    
                fecha_factura = request.form.get('fecha_factura')    
                cedula_cliente = request.form.get('cedula_cliente')    
                nombre_completo = request.form.get('nombre_completo')    
                direccion= request.form.get('direccion')
                telefono = request.form.get('telefono')    
                email = request.form.get('email')   
                valor_total = request.form.get('valor_total')
                id_cliente= request.form.get('id_cliente')
                id_usuario= request.form.get('id_usuario')
                id_detalle_factura = request.form.get('id_detalle_factura')

        # Actualizar el producto en la base de datos

                factura_modificar = Facturas(numero_factura,fecha_factura,cedula_cliente,nombre_completo,direccion,telefono,email,valor_total,id_cliente,id_usuario,id_detalle_factura)
               
                Facturas.actualizar_factura(factura_modificar,id_factura)
                
            
            
                return redirect(url_for('ver_facturas'))
        return render_template('formulario_login.html', titulo_pagina = 'Login')
        
        