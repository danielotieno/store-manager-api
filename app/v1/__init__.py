from flask import Flask
from flask_restful import Api

from config import app_config


def create_app(config_name):
    '''Function to create a flask app depending on the configuration passed'''

    app = Flask(__name__, instance_relative_config=True)
    api = Api(app)

    app.config.from_object(app_config[config_name])
    app.url_map.strict_slashes = False


    return app