import os
import sys
import cx_Oracle

if sys.platform.startswith("darwin"):
    cx_Oracle.init_oracle_client(lib_dir=os.environ.get("HOME")+"/desenvolvimento/instantclient_19_19")
elif sys.platform.startswith("win32"):
    cx_Oracle.init_oracle_client(lib_dir=r"c:\oracle\instantclient_19_19")
    
def init_session(connection, requestedTag_ignored):
    cursor = connection.cursor()
    cursor.execute("""
        ALTER SESSION SET
          TIME_ZONE = 'UTC'
          NLS_DATE_FORMAT = 'YYYY-MM-DD HH24:MI'""")


def start_pool():

    pool_min = 4
    pool_max = 4
    pool_inc = 0
    pool_gmd = cx_Oracle.SPOOL_ATTRVAL_WAIT
    
    un = 'cm' 
    pw = 'cm' 
    host           = 'dbclone.bpark.com.br'
    port           =  1521
    service_name   = 'desenv'
    
    dsn = f'{host}:{port}/{service_name}'

    print("Connecting to", os.environ.get("PYTHON_CONNECTSTRING"))

    pool = cx_Oracle.SessionPool(user=un,
                                 password=pw,
                                 dsn=dsn,
                                 min=pool_min,
                                 max=pool_max,
                                 increment=pool_inc,
                                 threaded=True,
                                 getmode=pool_gmd,
                                 sessionCallback=init_session)

    return pool

if __name__ == '__main__':
    pool = start_pool()

