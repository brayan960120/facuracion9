from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from src.models import session, Base
from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime

from src.models.usuarios import Usuarios
from src.models.detalle_facturas import DetalleFacturas
from sqlalchemy.orm import relationship



class Movimientos(Base):
    __tablename__ = 'movimientos'

    id = Column(Integer, primary_key=True)
    usuario_id = Column(
        Integer,
        ForeignKey('usuarios.id'),
        nullable=False
    )
    producto_id = Column(
        Integer,
        ForeignKey('productos.id'),
        nullable=False
    )
    cantidad = Column(Integer, nullable=False)
    valor_unitario = Column(Float, nullable=False)
    tipo_de_movimiento = Column(String(20), nullable=False)
    fecha = Column(DateTime, default=datetime.utcnow)

    # Relaciones
    usuario = relationship("Usuarios", back_populates="movimientos")
    producto = relationship("Productos", back_populates="movimientos")

    def __repr__(self):
        return f'<Movimiento {self.id}>'
    
  
    
