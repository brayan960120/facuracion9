from src.app import app
from flask import render_template, request, redirect, url_for, flash
from flask_controller import FlaskController
from src.models.detalle_factura import Detalles_factura
from src.models.productos import Productos
from src.models.facturas import Facturas


class Detalles_facuraController(FlaskController):
    @app.route('/crear_detalle_producto', methods=['POST','GET'])
    def crear_detalle_producto():
        if request.method == 'POST':
            precio_venta = request.form.get('Precio_venta')    
            id_factura = request.form.get('id_factura')    
            id_producto = request.form.get('id_producto')    
            if not precio_venta:
                flash('El precio de la venta es un campo obligatorio')   
            elif not id_factura:
                flash('El id de la factura es un campo obligatorio')     
            elif not id_producto:
                flash('El id del producto es un campo obligatorio')     
            else: 
                detalle_factura = Detalles_factura(precio_venta,id_factura,id_producto)
                Detalles_factura.agregar_detalle_factura(detalle_factura)
                return redirect(url_for('ver_detalles_factura'))
        detalle_factura = Detalles_factura.obtener_detalles_factura()
        return render_template('formulario_detalle_factura.html', titulo_pagina = 'Crear detalle de la factura', detalle_factura = detalle_factura)

    @app.route('/ver_detalle_factura')
    def ver_detalle_factura():
        detalles_factura = Detalles_factura.obtener_detalles_factura()
        return render_template('tabla_detalles_factura.html', titulo_pagina = 'Ver detalles de la factura', detalles_factura = detalles_factura)
    
        
    @app.route('/eliminar_detalle_factura/<id>')
    def eliminar_detalle_factura(id):
        Detalles_factura.eliminar_detalle_factura(id)
        detalles_factura = Detalles_factura.obtener_detalles_factura()
        return render_template('tabla_detalles_factura.html', titulo_pagina = 'Ver detalles de la factura', detalles_factura = detalles_factura)