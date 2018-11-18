from flask import Flask
from flask_restplus import Api
from flask import Blueprint

from .api_sqlutil import sql_api as ns1


def create_app():
    app = Flask(__name__)
    return app

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK RESTPLUS API BOILER-PLATE WITH JWT',
          version='1.0',
          description='a boilerplate for flask restplus web service'
          )

api.add_namespace(ns1, path='/sql')
