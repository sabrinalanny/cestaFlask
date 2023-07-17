from sqlalchemy import Column, Date, Integer
from sqlalchemy.orm import declarative_base
from flask_restx import fields

Base = declarative_base() 

class FuncionarioCesta(Base):
    
    __tablename__ = 'funcionario_cesta'
    __table_args__ = {'schema' : 'bpreceptor'}
    id_cesta = Column(Integer, primary_key=True)
    matricula = Column(Integer, name='matricula')
    data = Column(Date, name='data')
    
    def __repr__(self):
       return f"FuncionarioCesta(id_cesta='{self.id_cesta}', matricula='{self.matricula}', data='{self.data}')"
 