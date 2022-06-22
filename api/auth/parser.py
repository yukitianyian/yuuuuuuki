# -*- coding:utf-8 -*-
from flask import jsonify
from flask_restful.reqparse import RequestParser, Argument, Namespace
from flask_restful import abort


class NewArgument(Argument):
    def handle_validation_error(self, error, bundle_errors):
        msg = f"{self.name}参数错误"
        abort(jsonify(code_no="201", code_msg=msg))


class NewRequestParser(RequestParser):
    def __init__(self, argument_class=NewArgument, namespace_class=Namespace, trim=False, bundle_errors=False):
        super().__init__(argument_class, namespace_class, trim, bundle_errors)


auth_parser = NewRequestParser()
auth_parser.add_argument("user", location="json", type=str, required=True, trim=True, nullable=False)
auth_parser.add_argument("pwd", location="json", type=str, required=True, trim=True, nullable=False)
