from flask import request
from flask_restx import Resource, fields

from ..util.pessoaEventoDTO import PessoaEventoDTO
from ..service.pessoaEventoService import getAll, getByPessoaEvento, save, getTotalEntregue, getSobra, entrega
from ..service.eventoService import getByEventoId
from ..service.pessoaService import getByPessoaId

api = PessoaEventoDTO.api
_pessoaEvento = PessoaEventoDTO.pessoaEvento
_resource_fields = api.model('PessoaEventoDTO', {
    'idpessoa': fields.Integer,
    'idevento': fields.Integer,
})


@api.route('/')
class PessoaEventoDTOListAll(Resource):
    @api.doc('lista de pessoa x evento')
    @api.marshal_list_with(_pessoaEvento)
    def get(self):
        pessoaEventoList = getAll()
        
        return pessoaEventoList, 200
    
    @api.expect(_resource_fields)
    def post(self):
        data = request.get_json()    
        evento = getByEventoId(data['idevento'])
        if not evento:
            response_object = {
                'status': 'falha',
                'message': 'Evento não existe.',
            }
            return response_object, 404  
        pessoa = getByPessoaId(data['idpessoa'])
        if not pessoa:
            response_object = {
                'status': 'falha',
                'message': 'Pessoa não existe.',
            }
            return response_object, 404  
        entrega = getByPessoaEvento(data['idpessoa'], data['idevento'])
        print(entrega)
        if entrega:  
            response_object = {
                'status': 'falha',
                'message': 'Pessoa x Evento já cadastrado.',
            }
            return response_object, 409  
        save(data)
        response_object = {
            'status': 'sucesso',
            'message': 'Registrado com sucesso'
        }
        return response_object, 201  
    
@api.route('/entrega')
class PessoaEventoEntrega(Resource):
    @api.expect(_resource_fields)
    def post(self):
        data = request.get_json()    
        evento = getByEventoId(data['idevento'])
        if not evento:
            response_object = {
                'status': 'falha',
                'message': 'Evento não existe.',
            }
            return response_object, 404  
        pessoa = getByPessoaId(data['idpessoa'])
        if not pessoa:
            response_object = {
                'status': 'falha',
                'message': 'Pessoa não existe.',
            }
            return response_object, 404  
        pessoaEvento = getByPessoaEvento(data['idpessoa'], data['idevento'])
        if not pessoaEvento:
            response_object = {
                'status': 'falha',
                'message': 'Pessoa não está apta para receber.',
            }
            return response_object, 409   
        print(pessoaEvento[0].dataentrega)
        if pessoaEvento[0].dataentrega:  
            response_object = {
                'status': 'falha',
                'message': 'Evento já entregue.',
            }
            return response_object, 409  
        entrega(data)
        response_object = {
            'status': 'sucesso',
            'message': 'Registrado com sucesso'
        }
        return response_object, 201  

@api.route('/<idevento>/entregue')
class EventoTotal(Resource):
    @api.doc('Quantidade total do evento')
    def get(self, idevento):
        evento = getByEventoId(idevento)
        if not evento:
            response_object = {
                'status': 'falha',
                'message': 'Evento não existe.',
            }
            return response_object, 404  
        quantidade = getTotalEntregue(idevento)
        response_object = {
            'quantidade': quantidade
        }
        return response_object, 200
 
@api.route('/<idevento>/sobra')
class PessoaEventoSobra(Resource):
    @api.doc('Quantidade de sobra do evento')
    def get(self, idevento):
        evento = getByEventoId(idevento)
        if not evento:
            response_object = {
                'status': 'falha',
                'message': 'Evento não existe.',
            }
            return response_object, 404  
        quantidade = getSobra(idevento)
        response_object = {
            'quantidade': quantidade
        }
        return response_object, 200
