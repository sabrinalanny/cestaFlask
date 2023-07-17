from flask_restx import Api
from flask import Blueprint

from .main.controller.funcionarioController import api as funcionario_ns
from .main.controller.cestaController import api as cesta_ns
from .main.controller.funcionarioCestaController import api as funcionariocesta_ns
#from .main.controller.auth_controller import api as auth_ns

blueprint = Blueprint('api', __name__)
authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}

api = Api(
    blueprint,
    title='POC - Cesta BP',
    version='1.0',
    description='POC usando python - flask',
    #authorizations=authorizations,
    #security='apikey'
)

api.add_namespace(funcionario_ns, path='/funcionario')
api.add_namespace(cesta_ns, path='/cesta')
api.add_namespace(funcionariocesta_ns, path='/funcionariocesta')
#api.add_namespace(auth_ns)