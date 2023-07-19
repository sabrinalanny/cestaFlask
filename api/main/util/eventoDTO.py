from flask_restx import Namespace, fields

class EventoDTO:
    api = Namespace('evento', description='Evento')
    evento = api.model('evento', {
        'idevento': fields.Integer(required=True, description='ID'),
        'nome': fields.String(required=True, description='Nome'),
        'quantidade': fields.String(required=True, description='Quantidade'),
    })