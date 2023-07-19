from flask import Flask 
from flask import render_template
#from flask_sqlalchemy import SQLAlchemy

def create_app():
    app = Flask(__name__)
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://sabrina:S@br1na@mesqldesenv.com.br:3306/evento'
    #db = SQLAlchemy(app)

    #db.init_app(app)
    return app

if __name__ == "__main__":  
    app = create_app()  
    app.run(debug = True)
    #app.run(host="0.0.0.0", port=8000, debug=True)    
  