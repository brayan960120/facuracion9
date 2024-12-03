from src.app import app
from flask import render_template, request, redirect, url_for, flash
from flask_controller import FlaskController
from src.models.categorias import Categorias

class CategoriasController(FlaskController):
    @app.route('/crear_categoria', methods=['POST','GET'])
    def crear_categoria():
        if request.method == 'POST':
            categoria = request.form.get('categoria')
            if not categoria:
                flash('El nombre de la categoria es un campo obligatorio')    
            else:     
                categoria = Categorias(categoria)
                Categorias.agregar_categoria(categoria)
                return redirect(url_for('ver_categorias'))
        return render_template('formulario_crear_categoria.html', titulo_pagina = 'Crear categoria')

    @app.route('/ver_categorias')
    def ver_categorias():
        categorias = Categorias.obtener_categorias()
        return render_template('tabla_categorias.html', titulo_pagina = 'Ver categorias', categorias=categorias)
    
    
    @app.route('/eliminar_categorias/<id>')
    def eliminar_categoria(id):
        Categorias.eliminar_categoria(id)
        categorias = Categorias.obtener_categorias()
        return render_template('tabla_categorias.html', titulo_pagina = 'Ver categorias', categorias=categorias)
    

    @app.route('/actualizar_categoria/<id>', methods=['GET', 'POST'])
    def actualizar_categoria(id):
        if request.method == 'GET':
        # Lógica para mostrar el formulario de edición con los datos actuales del producto
            categoria= Categorias.obtener_categoria_por_id(id)
            return render_template('formulario_actualizar_categoria.html',titulo_pagina = 'Actualizar Categorias', categoria=categoria)

        if request.method == 'POST':
        # Lógica para procesar la actualización del 
            id_categoria = request.form.get('id')       
            categoria = request.form.get('categoria')
            

        # Actualizar el producto en la base de datos
            categoria_modificar= Categorias(categoria)
            Categorias.actualizar_categoria(categoria_modificar,id_categoria)
            
            
            return redirect(url_for('ver_categorias'))