from src.app import app
from flask import render_template, request, redirect, url_for, flash
from flask_controller import FlaskController
from src.models.productos import Productos
from src.models.usuarios import Usuarios
from src.models.compras import Compras
from flask import session


class ComprasController(FlaskController):
    @app.route('/crear_compra1/<id>', methods=['POST','GET'])
    
    def crear_compra(id):
        if 'email' in session:
            if request.method == 'POST':
                numero_factura = request.form.get('numero_factura')    
                precio_unitario  = request.form.get('precio_unitario')
                cantidad= request.form.get('cantidad') 
                precio_total = request.form.get('precio_total')       
                id_producto= request.form.get('id_producto')    
                id_usuario = request.form.get('id_usuario')
            
                compra = Compras(numero_factura, precio_unitario, cantidad, precio_total, id_producto, id_usuario)
                Compras.agregar_compras(compra)
                return redirect(url_for('/ver_compras'))
        
            productos = Productos.obtener_productos()
            usuarios = Usuarios.obtener_usuarios()
            return render_template('comprar1.html', usuarios=usuarios, productos = productos,  titulo_pagina = 'Crear compras')
        return render_template('formulario_login.html', titulo_pagina = 'Login')
        

    @app.route('/ver_compras')
    def ver_compras():
        compras = Compras.obtener_compras()
        return render_template('tabla_compras.html', titulo_pagina = 'Ver compras', compras=compras)
    
    """@app.route('/eliminar_facturas/<id>')
    def eliminar_factura(id):
        Facturas.eliminar_factura(id)
        facturas = Facturas.obtener_facturas()
        return render_template('tabla_facturas.html', titulo_pagina = 'Ver facturas', facturas = facturas)
    
    @app.route('/actualizar_factura/<id>', methods=['GET', 'POST'])
    def actualizar_factura(id):
        if request.method == 'GET':
        # Lógica para mostrar el formulario de edición con los datos actuales del producto
            factura = Facturas.obtener_factura_por_id(id)
            cliente = Clientes.obtener_clientes()
            usuario = Usuarios.obtener_usuarios()
            detalle_factura = Detalles_factura.obtener_detalles_factura()
            return render_template('formulario_actualizar_factura.html',titulo_pagina = 'Actualizar Facturas', factura = factura , cliente = cliente, usuario = usuario, detalle_factura = detalle_factura)

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
            id_cliente= request.form.get('id_cliente')
            id_usuario= request.form.get('id_usuario')

        # Actualizar el producto en la base de datos
            factura_modificar = Facturas(numero_factura,fecha_factura,cedula_cliente,nombre_completo,direccion,telefono,email,id_cliente,id_usuario)
            Facturas.actualizar_factura(factura_modificar,id_factura)
            
            
            return redirect(url_for('ver_facturas'))"""