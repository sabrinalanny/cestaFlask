from flask_restx import Namespace, fields

class FuncionarioCestaDTO:
    api = Namespace('funcionarioCesta', description='Funcionario x Cesta')
    funcionarioCesta = api.model('funcionarioCesta', {
        'id_cesta': fields.Integer(required=True, description='Id cesta'),
        'matricula': fields.String(required=True, description='Matricula'),
        'data': fields.Date(required=True, description='Data'),
    })