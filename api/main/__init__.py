from flask import Flask
#import api.connectionPool as connectionPool 
from flask.app import Flask
import os
import platform
import oracledb
import sqlalchemy as sa
from sqlalchemy.pool import NullPool

# Use your config
un = 'cm' 
pw = 'cm' 
host           = 'dbclone.bpark.com.br'
port           =  1521
service_name   = 'desenv'

d = None  # default suitable for Linux
if platform.system() == "Linux" and platform.machine() == "x86_64":   # macOS
  d = os.environ.get("HOME")+("/desenvolvimento/instantclient_19_19")
elif platform.system() == "Windows":
  d = r"C:\oracle\instantclient_19_19"
oracledb.init_oracle_client(lib_dir=d)

pool = oracledb.create_pool(user=un, password=pw,
                            host=host, port=port, service_name=service_name,
                            min=1, max=4, increment=1)

engine = sa.create_engine("oracle+oracledb://", creator=pool.acquire, poolclass=NullPool)

def create_app(config_name: str) -> Flask:
    app = Flask(__name__)
    #app.config.from_object(config_by_name[config_name])
   
    

    return app