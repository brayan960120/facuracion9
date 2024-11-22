from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy import update
from sqlalchemy_serializer import SerializerMixin
from src.models import session, Base
from src.models.categorias import Categorias 


class Productos(Base,SerializerMixin):
    __tablename__ = 'productos'
    id = Column(Integer, primary_key=True)
    descripcion = Column(String(300), unique=True, nullable=False)
    valor_unitario = Column(Float(10,8), nullable=False)
    unidad_medida = Column(String(3), nullable=False)
    cantida_stock = Column(Float(10,8), nullable=False)
    categoria = Column(Integer, ForeignKey('categorias.id'), nullable=False)

    def __init__(self, descripcion, valor_unitario, unidad_medida, cantida_stock, categoria):
        self.descripcion = descripcion
        self.valor_unitario = valor_unitario
        self.unidad_medida = unidad_medida
        self.cantida_stock = cantida_stock
        self.categoria = categoria

    def obtener_productos():
        productos = session.query(Productos, Categorias).join(Categorias, Productos.categoria == Categorias.id).all()
        print(productos)
        return productos
    
    def agregar_producto(producto):
        producto = session.add(producto)
        session.commit()
        return producto
    
    def eliminar_producto(id):
        producto = session.query(Productos).get(id)        
        session.delete(producto)
        session.commit()
        return producto
    
    def actualizar_producto(producto):
        producto_modificar = session.query(Productos).get(producto.id)
        producto_modificar.descripcion = producto.descripcion
        producto_modificar.valor_unitario = producto.valor_unitario
        producto_modificar.unidad_medida = producto.unidad_medida
        producto_modificar.cantida_stock = producto.cantida_stock
        producto_modificar.categoria = producto.categoria



        session.commit()      
        return producto
    
    def obtener_producto_por_id(id):
        producto = session.query(Productos).get(id)
        return producto.to_dict()
    

    

    
    