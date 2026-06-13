from sqlalchemy import Column, Integer, String, Float, ForeignKey
from src.models import session, Base
from src.models.movimientos import Movimientos
from src.models.usuarios import Usuarios
from src.models.detalle_facturas import DetalleFacturas



class Facturas(Base):
    __tablename__ = 'facturas'
    id = Column(Integer, primary_key=True)
    numero_factura = Column(String(20), unique=True, nullable=False)
    fecha_factura = Column(String(20), nullable=False)
    cedula_cliente = Column(String(30), nullable=False)
    nombre_completo = Column(String(200), nullable=False)
    direccion = Column(String(200), nullable=False)
    telefono = Column(String(200), nullable=False)
    email =  Column(String(500), nullable=False)
    valor_total = Column(Float, nullable=False)
    
    id_cliente = Column(Integer, ForeignKey('clientes.id'), nullable=False)
    id_usuario = Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    id_detalle_factura = Column(Integer, ForeignKey('detalle_facturas.id'), nullable=False)

    def __init__(self, numero_factura, fecha_factura, cedula_cliente, nombre_completo, direccion, telefono, email, valor_total, id_cliente, id_usuario,id_detalle_factura):
        self.numero_factura = numero_factura
        self.fecha_factura = fecha_factura
        self.cedula_cliente = cedula_cliente
        self.nombre_completo = nombre_completo
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
        self.valor_total = valor_total
        self.id_cliente = id_cliente
        self.id_usuario = id_usuario
        self.id_detalle_factura = id_detalle_factura

    def obtener_facturas():
        facturas = (session.query(Facturas, Clientes, Usuarios)
                           .join(Clientes, Facturas.id_cliente == Clientes.id)
                           .join(Usuarios, Facturas.id_usuario == Usuarios.id)
                           .join(DetalleFacturas, Facturas.id_detalle_factura == DetalleFacturas.id)).all()
        return facturas 

 
    
    def agregar_factura(factura):
        factura = session.add(factura)
        session.commit()
        return factura

    def eliminar_factura(id):
        factura = session.query(Facturas).get(id)        
        session.delete(factura)
        session.commit()
        return factura
    
    def obtener_factura_por_id(id):
        factura = session.query(Facturas).get(id)
        return factura
    
    def actualizar_factura(factura,id):
        factura_modificar = session.query(Facturas).get(id)
        
        

    
        factura_modificar.numero_factura = factura.numero_factura
        factura_modificar.fecha_factura = factura.fecha_factura
        factura_modificar.cedula_cliente = factura.cedula_cliente
        factura_modificar.nombre_completo = factura.nombre_completo
        factura_modificar.direccion = factura.direccion
        factura_modificar.telefono = factura.telefono
        factura_modificar.email= factura.email
        factura_modificar.valor_total = factura.valor_total
        factura_modificar.id_cliente = factura.id_cliente
        factura_modificar.id_usuario = factura.id_usuario
        factura_modificar.id_detalle_factura = factura.id_detalle_factura

        session.commit()      
        return factura
    

    def obtener_facturas_por_usuario(id):
        factura = session.query(Facturas).filter_by(id_usuario=id).first()
        return factura
    
    def obtener_facturas_por_cliente(id):
        factura = session.query(Facturas).filter_by(id_cliente=id).first()
        return factura
    
    def obtener_facturas_por_detalle_factura(id):
        factura = session.query(Facturas).filter_by(id_detalle_factura=id).first()
        return factura
    
