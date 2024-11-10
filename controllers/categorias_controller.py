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