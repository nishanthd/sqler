from flask import request, abort
from flask_restplus import Namespace, Resource, fields,reqparse
from flask import jsonify

sql_api = Namespace('sql', description='Cats related operations')

SqlModel = sql_api.model('sql', {
    'value': fields.String(required=True, description='SQL string to parse')
})


@sql_api.route('/parse')
class SqlController(Resource):
    @sql_api.expect(SqlModel, validate=True)
    def post(self):
        if not request.json:
            abort(400)
        return request.json;
