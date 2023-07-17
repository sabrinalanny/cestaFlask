from flask import request, jsonify
from flask_restx import Resource, fields

from ..util.cestaDTO import CestaDTO
from ..service.cestaService import getAll, getByNome, save, getById, delete

api = CestaDTO.api
_cesta= CestaDTO.cesta
_resource_fields = api.model('Cesta', {
    'nome': fields.String,
    'quantidade': fields.Integer,
})

@api.route('/')
class CestaListAll(Resource):
    @api.doc('lista de cestas')
    @api.marshal_list_with(_cesta)
    def get(self):
        cestas = getAll()
        print(cestas)
        return cestas, 200
    
    @api.expect(_resource_fields)
    #@api.marshal_list_with(_cesta)
    def post(self):
        data = request.get_json()    
        cesta = getByNome(data['nome'])
        if cesta:  
            response_object = {
                'status': 'falha',
                'message': 'Cesta já existe.',
            }
            return response_object, 409  
        save(data)
        response_object = {
            'status': 'sucesso',
            'message': 'Registrado com sucesso'
        }
        return response_object, 201  
    
@api.route('/<nome>', methods=['GET'])
@api.param('nome', 'Nome da cesta')
class CestaList(Resource):
    @api.doc('get cesta')
    def get(self, nome):
        cesta = getByNome(nome)
        if not cesta:
            response_object = {
                'status': 'falha',
                'message': 'Cesta não encontrada'
            }
            return response_object, 404
        else:       
            return cesta[0].json(), 200
        
@api.route('/<id>', methods=['DELETE'])
@api.param('id', 'Id da cesta')
class CestaId(Resource):
    @api.doc('delete cesta')
    def delete(self, id):
        cesta = getById(id)
        if not cesta:
            response_object = {
                'status': 'falha',
                'message': 'Cesta não encontrada'
            }
            return response_object, 404
        else:     
            print(cesta)
            delete(cesta[0])  
            response_object = {
                'status': 'sucesso',
                'message': 'Cesta deletada'
            }
            return response_object, 200
    
