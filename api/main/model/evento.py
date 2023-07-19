from sqlalchemy import Column, String, Integer
from flask_restx import fields
from flask_sqlalchemy import SQLAlchemy
from api.main import db

class Evento(db.Model):
    
    __tablename__ = 'evento'
    __table_args__ = {'schema' : 'evento'}
    
    idevento = db.Column(Integer, primary_key=True)
    nome = db.Column(String(150), name='nome')
    quantidade = db.Column(Integer, name='quantidade')
    
    def __repr__(self):
        return f"Evento(idevento={self.idevento}, nome='{self.nome}', quantidade={self.quantidade})"
   
    def json(self):
        return {'idevento': self.idevento,'nome': self.nome, 'quantidade': self.quantidade}
 