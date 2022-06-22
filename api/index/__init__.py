from flask import Blueprint
from flask_restful import Api

index_blue = Blueprint("index", __name__, url_prefix="/index")
index_api = Api(index_blue)

from .views import *
