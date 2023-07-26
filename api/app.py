from flask import Flask 
from flask import render_template
#from flask_sqlalchemy import SQLAlchemy

def create_app():
    app = Flask(__name__)
    return app

if __name__ == "__main__":  
    app = create_app()  
    app.run(debug = True)  
  