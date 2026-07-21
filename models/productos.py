from xmlrpc.client import boolean

from flask import redirect, url_for, render_template, request, session
from sqlalchemy import Boolean, Column, Integer, String, Float, ForeignKey
from sqlalchemy_serializer import SerializerMixin
from src.models import session, Base
from sqlalchemy import update
from src.models.categorias import Categorias
from src.models import session as db_session



class Productos(Base,SerializerMixin):
    __tablename__ = 'productos'
    id = Column(Integer, primary_key=True)
    descripcion = Column(String(300), nullable=False)
    valor_unitario = Column(Integer, nullable=False)
    unidad_medida = Column(String(3), nullable=False)
    cantida_stock = Column(Integer, nullable=False)
    categoria = Column(Integer, ForeignKey('categorias.id'), nullable=False)
    activo = Column(Boolean, default=True)
    
    

    def __init__(self, descripcion, valor_unitario, unidad_medida, cantida_stock, categoria, activo=True):
        self.descripcion = descripcion
        self.valor_unitario = valor_unitario
        self.unidad_medida = unidad_medida
        self.cantida_stock = cantida_stock
        self.categoria = categoria
        self.activo = activo

    def obtener_productos():
        producto = session.query(Productos, Categorias).join(Categorias).all()
        producto = session.query(Productos).all()
        return producto

    
    def agregar_producto(producto):
        session.add(producto)
        session.commit()
        return producto

    def eliminar_producto(id):
        producto = session.get(Productos, id)

        if producto:
            producto.activo = False
            session.commit()

    def actualizar_producto(producto, id):

        producto_modificar = db_session.get(Productos, id)

        if producto_modificar is None:
            return None

        producto_modificar.descripcion = producto.descripcion
        producto_modificar.valor_unitario = producto.valor_unitario
        producto_modificar.unidad_medida = producto.unidad_medida
        producto_modificar.cantida_stock = producto.cantida_stock
        producto_modificar.categoria = producto.categoria
        producto_modificar.activo = producto.activo

        db_session.commit()

        return producto_modificar


    @classmethod
    def obtener_producto_por_id(cls, id):
        return session.query(cls).filter_by(id=id).first()
    
    def obtener_categorias_por_producto(id):
        productos = session.query(Productos).filter_by(categoria=id).all()
        return productos
    def comprar(id):
        producto = session.query(Productos).get(id)
        return producto

    
    
    
    """def comprar():
        producto = session.query(Productos).get(id)   
        return producto"""


    
    

    

    
    

    

    
    


    
    

    

    
    

    

    
    