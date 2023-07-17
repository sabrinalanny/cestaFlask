import uuid
from api.main.model.cesta import Cesta
from .. import engine
from sqlalchemy import select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text

Session = sessionmaker(bind=engine)
session = Session()

def getAll():
    sql = select(Cesta) \
    .order_by(Cesta.nome)

    cestas = session.execute(sql).fetchall()
    
    list_ = []
    for cesta in cestas:
        list_.append(cesta[0])
    return list_    

def getByNome(nomeParam):
    sql = select(Cesta) \
    .where(Cesta.nome.ilike("%"+nomeParam+"%"))

    cesta_by_nome = session.execute(sql).fetchone()
    
    if cesta_by_nome:
        return list(cesta_by_nome)
    
def save(data):
    cestaPk = session.execute(text('select bpreceptor.cesta_seq.nextval from dual')).fetchone()
    nova_cesta = Cesta(id_cesta=cestaPk[0], nome=data['nome'], quantidade=data['quantidade'])
    save_changes(nova_cesta)
    
def save_changes(data):
    session.add(data)
    session.commit()
    
def delete(data):
    session.delete(data)
    session.commit() 
    
def getById(idParam):
    sql = select(Cesta) \
    .where(Cesta.id_cesta == idParam)
    cesta_by_id = session.execute(sql).fetchone()
    if cesta_by_id:
        return list(cesta_by_id)       
