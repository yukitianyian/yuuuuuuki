from flask import render_template, redirect, make_response, request
from flask_restful import Resource

from api.auth import auth_api
from api.auth.parser import auth_parser


class Login(Resource):
    def get(self):
        return make_response(render_template('/login/login.html'))

    def post(self):
        # request_data = auth_parser.parse_args(strict=True)
        print(request.json())
        return make_response(render_template('index.html'))


auth_api.add_resource(Login, '/login', endpoint="根据token获取协议支付权限")
