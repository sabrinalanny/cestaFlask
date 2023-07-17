import datetime
from api.main.model.funcionarioCesta import FuncionarioCesta
from api.main.model.cesta import Cesta
from .. import engine
from sqlalchemy import select, distinct, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text

Session = sessionmaker(bind=engine)
session = Session()

def getAll():
    sql = select(FuncionarioCesta) \
    .order_by(FuncionarioCesta.cesta)

    entregas = session.execute(sql).fetchall()
    print(entregas)
    list_ = []
    for entrega in entregas:
        list_.append(entrega[0])
    return list_    

def getByCestaFuncionario(idCestaParam, matriculaParam):
    sql = select(FuncionarioCesta) \
    .where(FuncionarioCesta.id_cesta == idCestaParam) \
    .where(FuncionarioCesta.matricula == matriculaParam)
   
    entrega = session.execute(sql).fetchone()
    
    if entrega:
        return list(entrega)
    
def save(data):
    entrega = FuncionarioCesta(id_cesta=data['id_cesta'], matricula=data['matricula'], data=datetime.date.today())
    save_changes(entrega)
    
def save_changes(data):
    session.add(data)
    session.commit()   
    
def getTotalEntregue(idCestaParam):
    sql = select(func.count(FuncionarioCesta.id_cesta)) \
        .where(FuncionarioCesta.id_cesta == idCestaParam)        
  
    total = session.execute(sql).fetchone()
        
    if total:        
        return total[0]
    return 0
    
def getSobra(idCestaParam):
    sql = select(Cesta) \
    .where(Cesta.id_cesta == idCestaParam)
    cesta = session.execute(sql).fetchone()
    total = getTotalEntregue(idCestaParam)
    return cesta[0].quantidade - total

