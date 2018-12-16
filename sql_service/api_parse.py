from flask import request, abort, Response
from flask_restplus import Namespace, Resource, fields, reqparse
from flask_cors import CORS,cross_origin
from flask import jsonify
from .models import SqlParseRequest, Parameter, SqlParseResponse
import utils
from exception_handler import ParametersMismatch

sql_api = Namespace(
    'sql_api', description='SQL util to parse and manipulate parameters.')
# CORS(sql_api)

@sql_api.route('/parse')
class SqlController(Resource):

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
