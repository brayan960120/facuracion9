from flask_sqlalchemy import SQLAlchemy
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

engine = create_engine("postgresql+psycopg2://postgres:brayan965214@localhost:5432/facuracion")

connection = engine.connect()

Base = declarative_base()
Base.metadata.bind = engine

Session = sessionmaker(bind=engine)

session = Session()

def actualizar_tabla():
    cursor = connection.cursor
    query = """UPDATE Productos set (descripcion,valor_unitario,unidad_medida,cantida_stock,categoria) values ('{producto_modificar.descripcion}','{producto_modificar.valor_unitario}','{producto_modificar.unidad_medida}',
    '{producto_modificar.cantida_stock}','{producto_modificar.categoria}') """
    cursor.execute(query)
    cursor.close()

