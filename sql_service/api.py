from flask import request, abort
from flask_restplus import Namespace, Resource
from flask import jsonify
from .models import SqlParseRequest, SqlParseResponse
import utils
from exception_handler import ParametersMismatch

sql_api = Namespace(
    'Query', description='SQL util to parse and modify parameters.')
# CORS(sql_api)


@sql_api.route('/parse')
class QueryParser(Resource):
    @sql_api.doc('hellodoc')
    @sql_api.expect(SqlParseRequest, validate=True)
    def post(self):
        if not request.json:
            abort(400)
        req_data = request.get_json()
        response = SqlParseResponse()
        response.query = req_data['query']
        try:
            response.parameters = utils.extractParams(response.query)
        except ParametersMismatch as error:
            response = jsonify(error.to_dict())
            response.status_code = error.status_code
            return response
        return response.serialize()


@sql_api.route('/construct')
class QueryConstructor(Resource):
    @sql_api.expect(SqlParseResponse, validate=True)
    def post(self):
        if not request.json:
            abort(400)
        req_data = request.get_json()
        return utils.construct(req_data['query'], req_data['parameters'])
