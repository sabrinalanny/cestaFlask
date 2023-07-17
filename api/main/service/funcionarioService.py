from api.main.model.funcionario import Funcionario
from .. import engine
from sqlalchemy import select
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()


def getAll():
    sql = select(Funcionario)
    func_by_matricula = session.execute(sql).fetchone()
    print(func_by_matricula)
    return list(func_by_matricula)


def getByMatricula(matriculaParam):
    sql = select(Funcionario) \
    .where(Funcionario.matricula == matriculaParam)

    func_by_matricula = session.execute(sql).fetchone()
    if func_by_matricula:
        return list(func_by_matricula)  
    