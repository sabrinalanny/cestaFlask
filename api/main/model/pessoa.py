from sqlalchemy import Column, String, Integer
from flask_sqlalchemy import SQLAlchemy
from api.main import db

class Pessoa(db.Model):
    
    __tablename__ = 'pessoa'
    #__table_args__ = {'schema' : 'evento'}
    idpessoa = db.Column(Integer, primary_key=True, name='idpessoa')
    codigo = db.Column(String(45), name='codigo')
    nome = db.Column(String(150), name='nome')
    
    def __repr__(self):
       return f"Pessoa(nome='{self.nome}', codigo='{self.codigo}')"
   
    def __json__(self):
        _json = {
            'nome': self.nome,
            'codigo': self.codigo
        }

        return _json