from src.app import app
from flask import render_template, request, redirect, url_for, flash,session
from flask_controller import FlaskController
from src.models.productos import Productos
from src.models.categorias import Categorias
from src.models.usuarios import Usuarios
from src.models.detalle_facturas import DetalleFacturas



class ProductosController(FlaskController):
    @app.route('/crear_producto', methods=['POST','GET'])
    def crear_producto():
        if 'email' in session:
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
        return render_template('formulario_login.html', titulo_pagina = 'Login')
    

    
    @app.route('/ver_productos')
    def ver_productos():
        if 'email' in session:
            productos = Productos.obtener_productos()
            return render_template('tabla_productos.html', titulo_pagina = 'Ver Productos', productos=productos)
        return render_template('formulario_login.html', titulo_pagina = 'Login')
    
        
    @app.route('/eliminar_producto/<id>')
    def eliminar_producto(id):
        Productos.eliminar_producto(id)
        productos = Productos.obtener_productos()
        return render_template('tabla_productos.html', titulo_pagina = 'Ver Productos', productos=productos)
    

    @app.route('/actualizar_producto/<id>', methods=['GET', 'POST'])
    def actualizar_producto(id):
        if 'email' in session:
            if request.method == 'GET':
        # Lógica para mostrar el formulario de edición con los datos actuales del producto
                producto= Productos.obtener_producto_por_id(id)
                categoria = Categorias.obtener_categorias()
                return render_template('formulario_actualizar_producto.html',titulo_pagina = 'Actualizar Productos', producto=producto, categoria=categoria)

            if request.method == 'POST':
        # Lógica para procesar la actualización del 
                id_producto = request.form.get('id')    
                descripcion = request.form.get('descripcion')    
                valor_unitario = request.form.get('valor_unitario')    
                unidad_medida = request.form.get('unidad_medida')    
                cantida_stock = request.form.get('cantida_stock')    
                categoria = request.form.get('categoria')
                print (descripcion)

        # Actualizar el producto en la base de datos
                producto_modificar = Productos(descripcion,valor_unitario,unidad_medida,cantida_stock,categoria)
                Productos.actualizar_producto(producto_modificar,id_producto)
            
            
                return redirect(url_for('ver_productos'))
        return render_template('formulario_login.html', titulo_pagina = 'login')
        
   
    
    @app.route('/comprar/<id>', methods=['GET', 'POST'])
    def comprar(id):
        if 'email' in session:
            if request.method == 'GET':
        # Lógica para mostrar el formulario de edición con los datos actuales del producto
                producto= Productos.obtener_producto_por_id(id)
                categoria = Categorias.obtener_categorias()
                return render_template('formulario_compras.html',titulo_pagina = 'Actualizar Productos', producto=producto, categoria=categoria)

            if request.method == 'POST':
                valor_unitario = request.form.get('precio_unitario')
                cantidad= request.form.get('cantidad') 
                valor_total = request.form.get('precio_total')       
                id_producto= request.form.get('id_producto')  
                id_usuario = request.form.get('id_usuario')
            
                compra = Compras(valor_unitario, cantidad,valor_total, id_producto, id_usuario)
                Compras.agregar_compras(compra,id_producto)
                return redirect(url_for('/comprar'))