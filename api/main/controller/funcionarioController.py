from flask import request
from flask_restx import Resource

from ..util.funcionarioDTO import FuncionarioDTO
from ..service.funcionarioService import getAll, getByMatricula

api = FuncionarioDTO.api
_funcionario = FuncionarioDTO.funcionario


@api.route('/')
class FuncionarioList(Resource):
    @api.doc('lista de funcionarios')
    @api.marshal_list_with(_funcionario, envelope='data')
    def get(self):
        return getAll()

    
@api.route('/<matricula>')
@api.param('matricula', 'Matricula do funcionario')
@api.response(404, 'Funcionario nao encontrado.')
class User(Resource):
    @api.doc('get funcionario')
    @api.marshal_with(_funcionario)
    def get(self, matricula):
        funcionario = getByMatricula(matricula)
        if not funcionario:
            api.abort(404)
        else:
            return funcionario