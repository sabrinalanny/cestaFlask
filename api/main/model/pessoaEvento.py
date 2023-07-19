from sqlalchemy import DateTime, Integer
from flask_sqlalchemy import SQLAlchemy
from api.main import db

class PessoaEvento(db.Model):
    
    __tablename__ = 'pessoa_evento'
    #__table_args__ = {'schema' : 'evento'}
    idpessoa_evento = db.Column(Integer, primary_key=True, name='idpessoa_evento')
    idpessoa = db.Column(Integer, name='idpessoa')
    idevento = db.Column(Integer, name='idevento')
    dataentrega = db.Column(DateTime, name='dataentrega')
    
    def __repr__(self):
       return f"PessoaEvento(idpessoa_evento='{self.idpessoa_evento}', idpessoa='{self.idpessoa}', idevento='{self.idevento}', dataentrega='{self.dataentrega}')"
 