from flask import request, abort, Response
from flask_restplus import Namespace, Resource, fields, reqparse
from flask import jsonify
from .models import SqlParseRequest, Parameter, SqlParseResponse

sql_api = Namespace(
    'sql', description='SQL util to parse and manipulate parameters.')


@sql_api.route('/parse')
class SqlController(Resource):
    @sql_api.expect(SqlParseRequest, validate=True)
    def post(self):
        if not request.json:
            abort(400)
        req_data = request.get_json()
        parameter = Parameter()
        parameter.name = 'user'
        parameter.value = 'nishanthd'
        response = SqlParseResponse()
        response.query = req_data['query']
        response.parameters = [parameter]

        return response.serialize()
