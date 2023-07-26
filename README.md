
# Rodar localmente 
Ajustar username, password e host do banco em api/main/__init__.py
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://<user>:<password>@mysqldesenv.bpark.com.br/evento'

```
source {path do projeto}/venv/bin/activate
python3 -m pip install -r requirements.txt 
python3 manage.py run

```

# Rodar no servidor
Ajustar path do projeto
```
python3 wsgi.py run
```

