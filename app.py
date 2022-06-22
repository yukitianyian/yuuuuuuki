from flask import Flask

from api.auth import auth_blue
from api.index import index_blue

app = Flask(__name__)

app.register_blueprint(auth_blue)
app.register_blueprint(index_blue)
# @app.route('/')
# def hello_world():  # put application's code here
#     return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
