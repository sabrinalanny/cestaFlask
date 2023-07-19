import datetime
from api.main.model.pessoaEvento import PessoaEvento
from api.main.model.evento import Evento
from sqlalchemy import select, distinct, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text
from api.main import db

def getAll():
    sql = select(PessoaEvento) \
    .order_by(PessoaEvento.dataentrega)

    entregas = db.session.execute(sql).fetchall()
    if entregas:
        list_ = []
        for entrega in entregas:
            list_.append(entrega[0])
       
        return list_    

def getByPessoaEvento(idPessoaParam, idEventoaParam):
    sql = select(PessoaEvento) \
    .where(PessoaEvento.idevento == idEventoaParam) \
    .where(PessoaEvento.idpessoa == idPessoaParam)
   
    entrega = db.session.execute(sql).fetchone()
    print(entrega)
    if entrega:
        return list(entrega)
    
def entrega(data):
    entrega = PessoaEvento(idevento=data['idevento'], idpessoa=data['idpessoa'], dataentrega=datetime.date.today())
    save_changes(entrega)

def save(data):
    entrega = PessoaEvento(idevento=data['idevento'], idpessoa=data['idpessoa'])
    save_changes(entrega)
    
def save_changes(data):
    db.session.add(data)
    db.session.commit()   
    
def getTotalEntregue(idEventoParam):
    sql = select(func.count(PessoaEvento.idevento)) \
        .where(PessoaEvento.idevento == idEventoParam)        
  #todo and data entrgue
    total = db.session.execute(sql).fetchone()
        
    if total:        
        return total[0]
    return 0
    
def getSobra(idEventoParam):
    sql = select(Evento) \
    .where(Evento.idevento == idEventoParam)
    evento = db.session.execute(sql).fetchone()
    total = getTotalEntregue(idEventoParam)
    return evento[0].quantidade - total

