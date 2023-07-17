from flask import request
from flask_restx import Resource, fields, marshal

from ..util.funcionarioCestaDTO import FuncionarioCestaDTO
from ..service.funcionarioCestaService import getAll, getByCestaFuncionario, save, getTotalEntregue, getSobra
from ..service.cestaService import getById
from ..service.funcionarioService import getByMatricula

api = FuncionarioCestaDTO.api
_funcionarioCesta= FuncionarioCestaDTO.funcionarioCesta
_resource_fields = api.model('FuncionarioCesta', {
    'id_cesta': fields.Integer,
    'matricula': fields.String,
})
_quantidade = api.model('FuncionarioCesta', {
    'quantidade': fields.Integer,
})

@api.route('/')
class FuncionarioCestaListAll(Resource):
    @api.doc('lista de funcionario x cesta')
    @api.marshal_list_with(_funcionarioCesta)
    def get(self):
        funcionarioCestaList = getAll()
        print(funcionarioCestaList)
        return funcionarioCestaList, 200
    
    @api.expect(_resource_fields)
    def post(self):
        data = request.get_json()    
        cesta = getById(data['id_cesta'])
        if not cesta:
            response_object = {
                'status': 'falha',
                'message': 'Cesta não existe.',
            }
            return response_object, 404  
        funcionario = getByMatricula(data['matricula'])
        if not funcionario:
            response_object = {
                'status': 'falha',
                'message': 'Funcionário não existe.',
            }
            return response_object, 404  
        entrega = getByCestaFuncionario(data['id_cesta'], data['matricula'])
        if entrega:  
            response_object = {
                'status': 'falha',
                'message': 'Cesta já entregue ao funcionário anteriormente.',
            }
            return response_object, 409  
        save(data)
        response_object = {
            'status': 'sucesso',
            'message': 'Registrado com sucesso'
        }
        return response_object, 201  

@api.route('/<id_cesta>/entregue')
class FuncionarioCestaTotal(Resource):
    @api.doc('Total de cestas')
    def get(self, id_cesta):
        cesta = getById(id_cesta)
        if not cesta:
            response_object = {
                'status': 'falha',
                'message': 'Cesta não existe.',
            }
            return response_object, 404  
        quantidade = getTotalEntregue(id_cesta)
        response_object = {
            'quantidade': quantidade
        }
        return response_object, 200
 
@api.route('/<id_cesta>/sobra')
class FuncionarioCestaSobra(Resource):
    @api.doc('Sobra de cestas')
    def get(self, id_cesta):
        cesta = getById(id_cesta)
        if not cesta:
            response_object = {
                'status': 'falha',
                'message': 'Cesta não existe.',
            }
            return response_object, 404  
        quantidade = getSobra(id_cesta)
        response_object = {
            'quantidade': quantidade
        }
        return response_object, 200
