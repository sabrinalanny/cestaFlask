from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base
from flask_restx import fields

Base = declarative_base() 

class Cesta(Base):
    
    __tablename__ = 'cesta'
    __table_args__ = {'schema' : 'bpreceptor'}
    
    id_cesta = Column(Integer, primary_key=True)
    nome = Column(String(100), name='nome')
    quantidade = Column(Integer, name='quantidade')
    
    def __repr__(self):
        return f"Cesta(id_cesta={self.id_cesta}, nome='{self.nome}', quantidade={self.quantidade})"
   
    def json(self):
        return {'id_cesta': self.id_cesta,'nome': self.nome, 'quantidade': self.quantidade}
 