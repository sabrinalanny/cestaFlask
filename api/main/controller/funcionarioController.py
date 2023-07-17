from flask import request, jsonify, make_response
from flask_restx import Resource, fields

from ..model.funcionario import Funcionario
from ..util.funcionarioDTO import FuncionarioDTO
from ..service.funcionarioService import getAll, getByMatricula

api = FuncionarioDTO.api
_funcionario = FuncionarioDTO.funcionario

@api.route('/', methods=['GET'])
class FuncionarioListAll(Resource):
    @api.doc('lista de funcionarios')
    @api.marshal_list_with(_funcionario)
    def get(self):
        return getAll()

    
@api.route('/<matricula>', methods=['GET'])
@api.param('matricula', 'Matricula do funcionario')
@api.response(404, 'Funcionario nao encontrado.')
class FuncionarioList(Resource):
    @api.doc('get funcionario')
    @api.marshal_with(_funcionario)
    def get(self, matricula):
        funcionario = getByMatricula(matricula)
        #print(funcionario)
        if not funcionario:
            api.abort(404)
        else:
            return funcionario
            