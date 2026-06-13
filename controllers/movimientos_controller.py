from flask import render_template, request, redirect, url_for, flash
from src.models import session  
from src.models.productos import Productos
from src.models.movimientos import Movimientos
from src.models.usuarios import Usuarios
from flask import render_template, request, redirect, url_for, flash,session, flash
from src.models import session 
from src.app import app


@app.route('/movimientos')
def movimientos():
    usuarios = session.query(Usuarios).all()
    productos = session.query(Productos).all()

    return render_template(
        'tabla_movimientos.html',
        usuarios=usuarios,
        productos=productos
    )


@app.route('/crear_movimiento', methods=['POST'])
def crear_movimiento():
    try:
        movimiento = Movimiento(
            usuario_id=request.form['usuario_id'],
            producto_id=request.form['producto_id'],
            cantidad=request.form['cantidad'],
            valor_unitario=request.form['valor_unitario'],
            tipo_de_movimiento=request.form['tipo_de_movimiento']
        )

        session.add(movimiento)
        session.commit()

        flash('Movimiento guardado correctamente', 'success')

    except Exception as e:
        session.rollback()
        flash(f'Error al guardar: {str(e)}', 'danger')

    return redirect(url_for('tabla_movimientos'))
    