from flask_restx import Namespace, fields

class CestaDTO:
    api = Namespace('cesta', description='Cesta')
    cesta = api.model('cesta', {
        'id_cesta': fields.Integer(required=True, description='ID'),
        'nome': fields.String(required=True, description='Nome'),
        'quantidade': fields.String(required=True, description='Quantidade'),
    })