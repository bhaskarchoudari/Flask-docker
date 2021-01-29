from flask import Flask, jsonify
from flask_restx import Resource, Api


# instantiate the app
app = Flask(__name__)

api = Api(app)

# set config
app.config.from_object('src.config.DevelopmentConfig')  # new


class Ping(Resource):
    def get(self):
        return {
        'status': 'success',
        'message': 'Hi Flask'
    }


api.add_resource(Ping, '/ping')