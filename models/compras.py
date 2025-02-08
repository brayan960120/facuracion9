from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy_serializer import SerializerMixin
from src.models import session, Base
from src.models.usuarios import Usuarios
from src.models.productos import Productos


class Compras(Base, SerializerMixin):
    __tablename__ = 'compras'
    id = Column(Integer, primary_key=True)
    numero_factura = Column(String(30), unique=True, nullable=False)
    precio_unitario = Column(Float, nullable=False )
    cantidad = Column(Integer, nullable=False)
    precio_total = Column(Float, nullable=False) 
    id_producto = Column(Integer,ForeignKey('productos.id'), nullable=False)
    id_usuario = Column(Integer, ForeignKey('usuarios.id'), nullable=False)

    def __init__(self, numero_factura, precio_unitario, cantidad, precio_total, id_producto, id_usuario):
        self.numero_factura = numero_factura
        self.precio_unitario = precio_unitario
        self.cantidad = cantidad
        self.precio_total = precio_total
        self.id_producto = id_producto
        self.id_usuario = id_usuario

    def obtener_compras():
        facturas = (session.query(Compras, Productos, Usuarios)
                           .join(Productos, Compras.id_producto == Productos.id)
                           .join(Usuarios, Compras.id_usuario == Usuarios.id)).all()
        return facturas 

    
    
    def agregar_compras(compra):
        compra = session.add(compra)
        session.commit()
        return compra
    
    def obtener_compra_por_id(id):
        compra = session.query(Compras).get(id)
        return compra.to_dict()
    

    
    
    """def eliminar_compra(id):
        cliente = session.query(Clientes).get(id)        
        session.delete(cliente)
        session.commit()
        return cliente
    
    def actualizar_compra(cliente,id):
        cliente_modificar = session.query(Clientes).get(id)
        

        cliente_modificar.numero_identificacion = cliente.numero_identificacion
        cliente_modificar.nombre_completo = cliente.nombre_completo
        cliente_modificar.direccion = cliente.direccion
        cliente_modificar.telefono = cliente.telefono
        cliente_modificar.email = cliente.email

        session.commit()      
        return cliente"""
    