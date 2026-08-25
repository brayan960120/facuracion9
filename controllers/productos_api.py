from flask import request, jsonify
from flask_controller import FlaskController
from src.models.usuarios import Usuarios
from src.app import app
from src.models.productos import Productos
from src.models import session as db_session


class ProductosAPIController(FlaskController):

    @app.route("/api/productos", methods=["GET"])
    def api_obtener_productos():

        productos = Productos.obtener_productos()

        resultado = []

        for producto, categoria in productos:

            resultado.append({
                "id": producto.id,
                "descripcion": producto.descripcion,
                "valor_unitario": producto.valor_unitario,
                "unidad_medida": producto.unidad_medida,
                "cantida_stock": producto.cantida_stock,

            # Aquí mandamos el NOMBRE
                "categoria": categoria.categoria,

                "activo": producto.activo
            })

        return jsonify(resultado)


    @app.route("/api/productos", methods=["POST"])
    def api_agregar_producto():

        datos = request.get_json()

        producto = Productos(
            descripcion=datos["descripcion"],
            valor_unitario=datos["valor_unitario"],
            unidad_medida=datos["unidad_medida"],
            cantida_stock=datos["cantida_stock"],
            categoria=datos["categoria"],
            activo=datos.get("activo", True)
        )

        Productos.agregar_producto(producto)

        return jsonify({
            "mensaje": "Producto creado correctamente",
            "id": producto.id
        }), 201

    @app.route("/api/productos/<int:id>", methods=["PUT"])
    def api_actualizar_producto(id):

        datos = request.get_json()

        producto = Productos.obtener_producto_por_id(id)

        if producto is None:
            return jsonify({
                "error": "Producto no encontrado"
            }), 404

        producto.descripcion = datos.get("descripcion", producto.descripcion)
        producto.valor_unitario = datos.get(
            "valor_unitario",
             producto.valor_unitario
        )
        producto.unidad_medida = datos.get(
            "unidad_medida",
            producto.unidad_medida
        )
        producto.cantida_stock = datos.get(
            "cantida_stock",
            producto.cantida_stock
        )
        producto.categoria = datos.get(
            "categoria",
            producto.categoria
        )

        if "activo" in datos:
            producto.activo = datos["activo"]

        db_session.commit()

        return jsonify({
            "mensaje": "Producto actualizado correctamente",
            "producto": {
                "id": producto.id,
                "descripcion": producto.descripcion,
                "valor_unitario": producto.valor_unitario,
                "unidad_medida": producto.unidad_medida,
                "cantida_stock": producto.cantida_stock,
                "categoria": producto.categoria,
                "activo": producto.activo
            }
        }), 200

    @app.route("/api/productos/<int:id>", methods=["DELETE"])
    def api_eliminar_producto(id):

        producto = Productos.obtener_producto_por_id(id)

        if producto is None:
            return jsonify({
                "error": "Producto no encontrado"
            }), 404

        producto.activo = False

        db_session.commit()

        return jsonify({
            "mensaje": "Producto desactivado correctamente"
        }), 200

    @app.route("/api/login", methods=["POST"])
    def api_login():

        datos = request.get_json()

        email = datos.get("email")
        contraseña = datos.get("contrasena")

        if not email or not contraseña:
            return jsonify({
                "error": "Email y contraseña son obligatorios"
            }), 400

        usuario = Usuarios.validar_usuario(email, contraseña)

        if not usuario:
            return jsonify({
                "error": "Email o contraseña incorrectos"
            }), 401

        return jsonify({
            "mensaje": "Login correcto",
            "usuario": {
                "id": usuario.id_usuario,
                "email": usuario.email,
                "nombre": usuario.nombre_completo
            }
        })