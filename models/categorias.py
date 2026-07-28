from sqlalchemy import Column, Integer, String
from src.models import session, Base
from sqlalchemy.orm import relationship


class Categorias(Base):
    __tablename__ = "categorias"    
    id = Column(Integer, primary_key=True)
    categoria = Column(String(300), nullable=False)


    def __init__(self, categoria):
        self.categoria = categoria


    def obtener_categorias():
        categorias = session.query(Categorias).all()
        return categorias
    
    def agregar_categoria(categoria):
        categoria = session.add(categoria)
        session.commit()
        return categoria
    
    def eliminar_categoria(id):
        categoria = session.query(Categorias).get(id)        
        session.delete(categoria)
        session.commit()
        return categoria
    
        
    def obtener_categoria_por_id(id):
        categoria = session.query(Categorias).get(id)
        return categoria
    

    
    def actualizar_categoria(categoria,id):
        print ("modelo categoria ", id)
        categoria_modificar = session.query(Categorias).get(id)
        categoria_modificar.categoria = categoria.categoria
        session.commit()      
        return categoria
    
    



    

    
    
    
    
    
    



    

    
    
    
    
    
    
