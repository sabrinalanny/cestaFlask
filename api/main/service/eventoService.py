import uuid
from api.main.model.evento import Evento
from sqlalchemy import select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text
from flask_sqlalchemy import SQLAlchemy
from api.main import db

def getAll():
    sql = select(Evento) \
    .order_by(Evento.nome)

    eventos = db.session.execute(sql).fetchall()
    
    if eventos:
        list_ = []
        for evento in eventos:
            list_.append(evento[0])
        return list_    

def getByNome(nomeParam):
    sql = select(Evento) \
    .where(Evento.nome.ilike("%"+nomeParam+"%"))

    eventos_by_nome = db.session.execute(sql).fetchall()
    
    list_ = []
    for evento in eventos_by_nome:
        list_.append(evento[0])
    return list_ 
    
def save(data):
    novo_evento = Evento(nome=data['nome'], quantidade=data['quantidade'])
    save_changes(novo_evento)
    
def save_changes(data):
    db.session.add(data)
    db.session.commit()
    
def delete(data):
    db.session.delete(data)
    db.session.commit() 
    
def getByEventoId(idParam):
    sql = select(Evento) \
    .where(Evento.idevento == idParam)
    evento_by_id = db.session.execute(sql).fetchone()
    if evento_by_id:
        return list(evento_by_id)       
