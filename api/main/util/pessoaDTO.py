from flask_restx import Namespace, fields

class PessoaDTO:
    api = Namespace('pessoa', description='Pessoa')
    pessoa = api.model('pessoa', {
        'idpessoa': fields.Integer(required=True, description='ID'),
        'codigo': fields.String(required=True, description='Código'),
        'nome': fields.String(required=True, description='Nome'),
    })