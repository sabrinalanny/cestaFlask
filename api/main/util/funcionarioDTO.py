from flask_restx import Namespace, fields


class FuncionarioDTO:
    api = Namespace('funcionario', description='Funcionario')
    funcionario = api.model('funcionario', {
        'matricula': fields.String(required=True, description='Matricula'),
        'nome': fields.String(required=True, description='Nome'),
    })