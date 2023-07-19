from flask_restx import Namespace, fields

class PessoaEventoDTO:
    api = Namespace('pessoaEvento', description='Pessoa x Evento')
    pessoaEvento = api.model('pessoaEvento', {
        'idpessoa_evento': fields.Integer(required=True),
        'idpessoa': fields.String(required=True),
        'idevento': fields.String(required=True),
        'dataentrega': fields.Date(required=True),
    })