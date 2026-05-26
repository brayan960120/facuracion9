from src.app import app
from flask import render_template, request, redirect, url_for, flash
from flask_controller import FlaskController
from src.models.productos import Productos
from src.models.usuarios import Usuarios
from src.models.facturas import Facturas
from src.models.detalle_facturas import DetalleFacturas
from flask import session


class DetalleFacturasController(FlaskController):
    @app.route('/compra2/<id>', methods=['POST','GET'])
    
    def crear_detalle_factura(id):
        if 'email' in session:
            if request.method == 'POST':
                valor_unitario = request.form.get('valor_unitario')
                cantidad= request.form.get('cantidad') 
                valor_total = request.form.get('valor_total')       
                id_producto= request.form.get('id_producto')  
                id_usuario = request.form.get('id_usuario')

                detalle_factura = DetalleFacturas(valor_unitario, cantidad, valor_total, id_producto, id_usuario)
                DetalleFacturas.agregar_detalle_factura(detalle_factura)
                return redirect(url_for('ver_detalle_facturas'))
        
            producto= Productos.obtener_producto_por_id(id)
            usuarios= Usuarios.obtener_usuarios()
            print(producto)
            return render_template('formulario_compras.html', producto=producto, usuarios=usuarios, titulo_pagina = 'Crear compras')
        return render_template('formulario_login.html', titulo_pagina = 'Login')
        
    @app.route('/ver_detalle_facturas')
    def ver_detalle_facturas():
        if 'email' in session:
            detalle_facturas = DetalleFacturas.obtener_detalle_facturas()
            return render_template('tabla_detalle_facturas.html', titulo_pagina = 'Ver Detalles de Facturas', detalle_facturas=detalle_facturas)
        return render_template('formulario_login.html', titulo_pagina = 'Login')
                
            
    @app.route('/eliminar_detalle_factura/<id>')
    def eliminar_detalle_factura(id):
        if Facturas.obtener_facturas_por_detalle_factura(id):
            flash('No se puede eliminar la compra porque tiene facturas asociadas.')
            detalle_facturas = DetalleFacturas.obtener_detalle_facturas()
            return render_template('tabla_detalle_facturas.html', titulo_pagina= 'Ver Detalles de Facturas', detalle_facturas=detalle_facturas)
        else:
            DetalleFacturas.eliminar_detalle_factura(id)
            detalle_facturas= DetalleFacturas.obtener_detalle_facturas()
            return render_template('tabla_detalle_facturas.html',  titulo_pagina= 'Ver Detalles de Facturas', detalle_facturas = detalle_facturas)
    

    @app.route('/actualizar_detalle_factura/<id>', methods=['GET', 'POST'])
    def actualizar_detalle_factura(id):
        if 'email' in session:
            if request.method == 'GET':

                detalle_facturas = DetalleFacturas.obtener_detalle_facturas()
                producto = Productos.obtener_productos()
                detalle_factura = DetalleFacturas.obtener_detalle_facturas_por_id(id)
                usuario = Usuarios.obtener_usuarios()
                return render_template('formulario_actualizar_detalle_factura.html', detalle_factura=detalle_factura, detalle_facturas=detalle_facturas, usuario=usuario, producto=producto, titulo_pagina = 'Actualizar Detalle de Factura')
            
            if request.method == 'POST':


                id_detalle_factura = request.form.get('id')
                valor_unitario = request.form.get('valor_unitario')
                cantidad= request.form.get('cantidad') 
                valor_total = request.form.get('valor_total')       
                id_producto= request.form.get('id_producto')  
                id_usuario = request.form.get('id_usuario')
                
                detalle_factura_modificar = DetalleFacturas(valor_unitario, cantidad, valor_total, id_producto, id_usuario)
                DetalleFacturas.actualizar_detalle_factura(detalle_factura_modificar, id_detalle_factura)
                return redirect(url_for('ver_detalle_facturas') )

        return render_template('formulario_login.html', titulo_pagina = 'Login')
                
                