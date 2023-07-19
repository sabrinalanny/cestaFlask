from api.main.model.pessoa import Pessoa
from sqlalchemy import select
from sqlalchemy.orm import sessionmaker
from flask_sqlalchemy import SQLAlchemy
from api.main import db

def getAll():
    sql = select(Pessoa)
    pessoas = db.session.execute(sql).fetchall()
    if pessoas:
        list_ = []
        for pessoa in pessoas:
            list_.append(pessoa[0])
        return list_  

def getByCodigo(codigoParam):
    sql = select(Pessoa) \
    .where(Pessoa.codigo == codigoParam)
    pessoas = db.session.execute(sql).fetchone()
    if pessoas:
        return list(pessoas)
    
    
def save(data):
    nova_pessoa = Pessoa(codigo=data['codigo'], nome=data['nome'])
    save_changes(nova_pessoa)
    
def save_changes(data):
    db.session.add(data)
    db.session.commit()
    
def delete(data):
    db.session.delete(data)
    db.session.commit() 
    
def delete(data):
    db.session.delete(data)
    db.session.commit() 
    
def getByPessoaId(idParam):
    sql = select(Pessoa) \
    .where(Pessoa.idpessoa == idParam)
    pessoa_by_id = db.session.execute(sql).fetchone()
    if pessoa_by_id:
        return list(pessoa_by_id)       

   