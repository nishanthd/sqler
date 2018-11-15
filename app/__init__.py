from flask_restplus import Api
from flask import Blueprint

from .main.controller.sql_controller import sql_api as ns1

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK RESTPLUS API BOILER-PLATE WITH JWT',
          version='1.0',
          description='a boilerplate for flask restplus web service'
          )

api.add_namespace(ns1, path='/sql')
