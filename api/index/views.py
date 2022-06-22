from flask import render_template, redirect, make_response
from flask_restful import Resource

from api.auth import auth_api
from api.auth.parser import auth_parser
from api.index import index_api


class Index(Resource):
    def get(self):
        return make_response(render_template('index.html'))


index_api.add_resource(Index, "/123")
