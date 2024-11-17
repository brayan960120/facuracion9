from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy_serializer import SerializerMixin
from src.models import session, Base
from src.models.productos import Productos
from src.models.facturas import Facturas


class Detalles_factura(Base, SerializerMixin):
    __tablename__ = 'detalles_factura'
    id = Column(Integer, primary_key=True)
    precio_venta = Column(String(30), nullable=False)
    id_factura = Column(Integer, ForeignKey('facturas.id'), nullable=False)
    id_producto = Column(Integer, ForeignKey('productos.id'), nullable=False)


    def __init__(self, precio_venta, id_factura, id_producto):
        self.precio_venta = precio_venta
        self.id_factura = id_factura
        self.id_producto = id_producto


    def obtener_detalles_factura():
        detalles_factura = (session.query(Facturas, Detalles_factura, Productos)
                           .join(Facturas, Detalles_factura.id_factura == Facturas.id)
                           .join(Productos, Detalles_factura.id_producto == Productos.id)).all()
        return detalles_factura
    
    def agregar_detalle_factura(detalle_factura):
        detalle_factura = session.add(detalle_factura)
        session.commit()
        return detalle_factura
    
    def eliminar_detalle_factura(id):
        detalle_factura = session.query(Detalles_factura).get(id)        
        session.delete(detalle_factura)
        session.commit()
        return detalle_factura



    