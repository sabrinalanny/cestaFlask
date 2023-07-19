from flask import request, jsonify, make_response
from flask_restx import Resource, fields

from ..model.pessoa import Pessoa
from ..util.pessoaDTO import PessoaDTO
from ..service.pessoaService import getAll, getByCodigo, save, getByPessoaId, delete

api = PessoaDTO.api
_pessoa = PessoaDTO.pessoa
_resource_fields = api.model('Pessoa', {
    'codigo': fields.String,
    'nome': fields.String,
})

@api.route('/')
class PessoaListAll(Resource):
    @api.doc('lista de pessoas')
    @api.marshal_list_with(_pessoa)
    def get(self):
        pessoas = getAll()
        return pessoas, 200
    
    @api.expect(_resource_fields)
    def post(self):
        data = request.get_json()    
        evento = getByCodigo(data['codigo'])
        if evento:  
            response_object = {
                'status': 'falha',
                'message': 'Pessoa já existe.',
            }
            return response_object, 409  
        save(data)
        response_object = {
            'status': 'sucesso',
            'message': 'Registrado com sucesso'
        }
        return response_object, 201  
    
@api.route('/<codigo>', methods=['GET'])
@api.param('codigo', 'Código da pessoa')
class PessoaList(Resource):
    @api.doc('get pessoa')
    @api.marshal_list_with(_pessoa)
    def get(self, codigo):
        pessoa = getByCodigo(codigo)        
        if not pessoa:
            response_object = {
                'status': 'falha',
                'message': 'Pessoa não encontrada'
            }
            return response_object, 404
        else:       
            return pessoa, 200
            
@api.route('/<id>', methods=['DELETE'])
@api.param('id', 'Id da pessoa')
class PessoaId(Resource):
    @api.doc('delete pessoa')
    def delete(self, id):
        pessoa = getByPessoaId(id)
        if not pessoa:
            response_object = {
                'status': 'falha',
                'message': 'Pessoa não encontrada'
            }
            return response_object, 404
        else:     
            delete(pessoa[0])  
            response_object = {
                'status': 'sucesso',
                'message': 'Pessoa deletada'
            }
            return response_object, 200
    
