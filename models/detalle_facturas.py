from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy_serializer import SerializerMixin
from src.models import session, Base



class DetalleFacturas(Base, SerializerMixin):
    __tablename__ = 'detalle_facturas'
    id = Column(Integer, primary_key=True)
    valor_unitario = Column(Float, nullable=False )
    cantidad = Column(Integer, nullable=False)
    valor_total = Column(Float, nullable=False) 
    id_producto = Column(Integer,ForeignKey('productos.id'), nullable=False)
    id_usuario = Column(Integer, ForeignKey('usuarios.id'), nullable=False)

    def __init__(self, valor_unitario, cantidad, valor_total, id_producto, id_usuario):
        self.valor_unitario = valor_unitario
        self.cantidad = cantidad
        self.valor_total = valor_total
        self.id_producto = id_producto
        self.id_usuario = id_usuario

    def obtener_detalle_facturas():
        detalle_facturas = (session.query(DetalleFacturas, Productos, Usuarios)
                           .join(Productos, DetalleFacturas.id_producto == Productos.id)
                           .join(Usuarios, DetalleFacturas.id_usuario == Usuarios.id)).all()
        return detalle_facturas
    
    def agregar_detalle_factura(detalle_factura):
        detalle_factura = session.add(detalle_factura)
        session.commit()
        return detalle_factura
    
    def obtener_detalle_facturas_por_id(id):
        detalle_factura = session.query(DetalleFacturas).get(id)
        return detalle_factura  
    
    def eliminar_detalle_factura(id):
        detalle_factura = session.query(DetalleFacturas).get(id)
        session.delete(detalle_factura)
        session.commit()
        return detalle_factura
    
    def actualizar_detalle_factura(detalle_factura,id):
        detalle_factura_modificar = session.query(DetalleFacturas).get(id)
        
        detalle_factura_modificar.valor_unitario = detalle_factura.valor_unitario
        detalle_factura_modificar.cantidad = detalle_factura.cantidad
        detalle_factura_modificar.valor_total = detalle_factura.valor_total
        detalle_factura_modificar.id_producto = detalle_factura.id_producto
        detalle_factura_modificar.id_usuario = detalle_factura.id_usuario

        session.commit()      
        return detalle_factura
    
    def obtener_detalle_facturas_por_usuario(id):
        factura = session.query(DetalleFacturas).filter_by(id_usuario=id).first()
        return factura
    

    
    

    
    