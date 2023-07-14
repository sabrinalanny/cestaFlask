import cx_Oracle
import os
import platform

print("entrou")
d = None  # default suitable for Linux
if platform.system() == "Linux" and platform.machine() == "x86_64":   # macOS
  d = os.environ.get("HOME")+("/desenvolvimento/instantclient_19_19")
elif platform.system() == "Windows":
  d = r"C:\oracle\instantclient_19_19"
cx_Oracle.init_oracle_client(lib_dir=d)

un = 'cm' 
pw = 'cm' 
host           = 'dbclone.bpark.com.br'
port           =  1521
service_name   = 'desenv'

#params = oracledb.ConnectParams(host=host, port=port, service_name=service_name)
#with oracledb.connect(user=un, password=pw, params = params) as connection:
dsn = f'{un}/{pw}@{host}:{port}/{service_name}'
print(dsn)
connection = cx_Oracle.connect(dsn) 
with connection as connection:
    with connection.cursor() as cursor:
        sql = """select * from cm.pessoa where rownum=1"""
        for r in cursor.execute(sql):
            print(r)


