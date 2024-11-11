from sqlalchemy import Column, Integer, String
from src.models import session, Base

class Usuarios(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True)
    nombre_completo = Column(String(200))
    email = Column(String(500), unique=True, nullable=False)
    contraseña = Column(String(30),unique=True, nullable=False)
    rol = Column(String(30), nullable=False)

    def __init__(self, nombre_completo, email, contraseña, rol):
        self.nombre_completo = nombre_completo
        self.email = email
        self.contraseña = contraseña
        self.rol = rol

    def obtener_usuarios():
        usuarios = session.query(Usuarios).all()
        return usuarios
    
    def agregar_usuario(usuario):
        usuario = session.add(usuario)
        session.commit()
        return usuario
    
    def eliminar_usuario(id):
        usuario = session.query(Usuarios).get(id)        
        session.delete(usuario)
        session.commit()
        return usuario
       
   