from flask import Flask 
import connexion 
from flask import render_template

#app = connexion.App(__name__, specification_dir="./")
app = Flask(__name__)
#app.add_api("swagger.yml")

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":    
    app.run(debug = True)
    #app.run(host="0.0.0.0", port=8000, debug=True)    
  