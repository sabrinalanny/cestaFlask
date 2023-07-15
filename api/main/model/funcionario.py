from sqlalchemy import Column, String
from sqlalchemy.orm import declarative_base

Base = declarative_base() 

class Funcionario(Base):
    
    __tablename__ = 'zfuncionario'
    __table_args__ = {'schema' : 'rm'}
    matricula = Column(String(57), primary_key=True)
    nome = Column(String(120), name='nome')
    
    #def __repr__(self):
    #    return "<Funcionario '{}'>".format(self.nome)
    def __repr__(self):
       return f"Funcionario(nome='{self.nome}', matricula='{self.matricula}')"