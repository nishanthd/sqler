from flask import Flask
from flask_restplus import Api
from flask_cors import CORS
from flask import Blueprint

from .api import sql_api as ns1


def create_app():
    app = Flask(__name__)
    CORS(app)
    return app


blueprint = Blueprint('api', __name__)
CORS(blueprint)
api = Api(blueprint,
          title='FLASK RESTPLUS API BOILER-PLATE WITH JWT',
          version='1.0',
          description='a boilerplate for flask restplus web service'
          )


api.add_namespace(ns1, path='/query')
