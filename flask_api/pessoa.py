
import connection 
from flask import jsonify

pool = connection.start_pool()

def read_all():    
    with pool.acquire() as con:
        with con.cursor() as cur:
            cur.arraysize = 1000
            pessoas = []
            for row in cur.execute("select idpessoa, nome from cm.pessoa p where idpessoa in (1,2,3)"):
                #pessoas = {'idpessoa': row[0], 'nome': row[1]}
                pessoas.append(row[1])
            return jsonify(pessoas)

def read_one(id):
    with pool.acquire() as con:
        with con.cursor() as cursor:    
            cursor.execute("select nome from cm.pessoa p where idpessoa = :id", id)
            r = cursor.fetchone()
            return (r[0] if r else "pessoa não encontrada")
