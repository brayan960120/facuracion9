from src.app import app
from flask import render_template, request, redirect, url_for, flash
from flask_controller import FlaskController
from src.models.productos import Productos
from src.models.categorias import Categorias

class ProductosController(FlaskController):
    @app.route('/crear_producto', methods=['POST','GET'])
    def crear_producto():
        if request.method == 'POST':
            descripcion = request.form.get('descripcion')    
            valor_unitario = request.form.get('valor_unitario')    
            unidad_medida = request.form.get('unidad_medida')    
            cantida_stock = request.form.get('cantida_stock')    
            categoria = request.form.get('categoria')
            if not descripcion:
                flash('La descripción es un campo obligatorio')   
            elif not valor_unitario:
                flash('El valor unitario es un campo obligatorio')     
            elif not unidad_medida:
                flash('La unidad de medida es un campo obligatorio')    
            elif not cantida_stock:
                flash('La cantidad en stock es un campo obligatorio')    
            elif not categoria:
                flash('La categoria es un campo obligatorio')  
            else: 
                producto = Productos(descripcion,valor_unitario,unidad_medida,cantida_stock,categoria)
                Productos.agregar_producto(producto)
                return redirect(url_for('ver_productos'))
        categoria = Categorias.obtener_categorias()
        return render_template('formulario_crear_producto.html', titulo_pagina = 'Crear Producto', categoria=categoria)

    @app.route('/ver_productos')
    def ver_productos():
        productos = Productos.obtener_productos()
        return render_template('tabla_productos.html', titulo_pagina = 'Ver Productos', productos=productos)
    
        
    @app.route('/eliminar_producto/<id>')
    def eliminar_producto(id):
        Productos.eliminar_producto(id)
        productos = Productos.obtener_productos()
        return render_template('tabla_productos.html', titulo_pagina = 'Ver Productos', productos=productos)
    
         
    @app.route('/actualizar_producto')
    def actualizar_producto():
        Productos.actualizar_producto()
        productos = Productos.obtener_productos()
        return render_template('formulario_actualizar_producto.html', titulo_pagina = 'Actualizar productos', productos=productos)
  