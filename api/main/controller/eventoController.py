from flask import request, jsonify
from flask_restx import Resource, fields

from ..util.eventoDTO import EventoDTO
from ..service.eventoService import getAll, getByNome, save, getByEventoId, delete

api = EventoDTO.api
_evento= EventoDTO.evento
_resource_fields = api.model('Evento', {
    'nome': fields.String,
    'quantidade': fields.Integer,
})

@api.route('/')
class EventoListAll(Resource):
    @api.doc('lista de eventos')
    @api.marshal_list_with(_evento)
    def get(self):
        eventos = getAll()
        print(eventos)
        return eventos, 200
    
    @api.expect(_resource_fields)
    def post(self):
        data = request.get_json()    
        evento = getByNome(data['nome'])
        if evento:  
            response_object = {
                'status': 'falha',
                'message': 'Evento já existe.',
            }
            return response_object, 409  
        save(data)
        response_object = {
            'status': 'sucesso',
            'message': 'Registrado com sucesso'
        }
        return response_object, 201  
    
@api.route('/<nome>', methods=['GET'])
@api.param('nome', 'Nome do evento')
class EventoList(Resource):
    @api.doc('get evento')
    @api.marshal_list_with(_evento)
    def get(self, nome):
        eventos = getByNome(nome)
        if not eventos:
            response_object = {
                'status': 'falha',
                'message': 'Evento não encontrado'
            }
            return response_object, 404
        else:       
            return eventos, 200
        
@api.route('/<id>', methods=['DELETE'])
@api.param('id', 'Id do evento')
class EventoId(Resource):
    @api.doc('delete evento')
    def delete(self, id):
        evento = getByEventoId(id)
        if not evento:
            response_object = {
                'status': 'falha',
                'message': 'Evento não encontrado'
            }
            return response_object, 404
        else:     
            print(evento)
            delete(evento[0])  
            response_object = {
                'status': 'sucesso',
                'message': 'Evento deletado'
            }
            return response_object, 200
    
