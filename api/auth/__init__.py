from flask import Blueprint
from flask_restful import Api

auth_blue = Blueprint("auth", __name__, url_prefix="/auth")
auth_api = Api(auth_blue)

from .views import *
