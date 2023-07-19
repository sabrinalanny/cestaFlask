from flask import Flask
#import api.connectionPool as connectionPool 
#from flask.app import Flask
#import os
#import platform
#import oracledb
from flask_sqlalchemy import SQLAlchemy
#from sqlalchemy.pool import NullPool
#from . import db

#un = 'cm' #os.getenv('DB_USER')
#pw = 'cm' #os.getenv('DB_PASSWORD')
#host = 'dbclone.bpark.com.br' #os.getenv('DB_HOST')
#port = '1521' #os.getenv('DB_PORT')
#service_name = 'desenv' #os.getenv('DB_SERVICE')

#d = None  # default suitable for Linux
#if platform.system() == "Linux" and platform.machine() == "x86_64":   # macOS
#  d = ("/usr/lib/instantclient")
#elif platform.system() == "Windows":
#  d = r"C:\oracle\instantclient"
#oracledb.init_oracle_client(lib_dir=d)

#pool = oracledb.create_pool(user=un, password=pw,
#                            host=host, port=port, service_name=service_name,
#                            min=1, max=4, increment=1)
#
#engine = sa.create_engine("oracle+oracledb://", creator=pool.acquire, poolclass=NullPool)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@server/db'
db = SQLAlchemy()

def create_app(config_name: str) -> Flask:
    app = Flask(__name__)
    #app.config.from_object(config_by_name[config_name])
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://sabrina:S%40br1na@mysqldesenv.bpark.com.br/evento'
    db.init_app(app)

    return app
