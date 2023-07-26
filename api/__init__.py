from flask_restx import Api
from flask import Blueprint

from .main.controller.pessoaController import api as pessoa_ns
from .main.controller.eventoController import api as evento_ns
from .main.controller.pessoaEventoController import api as pessoaEvento_ns
#from .main.controller.auth_controller import api as auth_ns
#from flask_sqlalchemy import SQLAlchemy


blueprint = Blueprint('api', __name__, url_prefix='/eventoapi')
#authorizations = {
#    'apikey': {
#        'type': 'apiKey',
#        'in': 'header',
#        'name': 'Authorization'
#    }
#}

api = Api(
    blueprint,
    title='POC - Entrega evento BP',
    version='1.0',
    description='POC usando python - flask',
    #authorizations=authorizations,
    #security='apikey'
)
api.default_namespace = api.namespace("default", "default_label",
            endpoint='{0}-declaration'.format("default"),
            validate="validate",
            api=api,
            path='/eventoapi',
        )

api.add_namespace(pessoa_ns, path='/pessoa')
api.add_namespace(evento_ns, path='/evento')
api.add_namespace(pessoaEvento_ns, path='/eventopessoa')
#api.add_namespace(auth_ns)