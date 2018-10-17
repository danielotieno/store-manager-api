import os

from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager

from config import app_config

jwt = JWTManager()


def create_app(config_name):
    """Function to create a flask app depending on the configuration passed"""

    app = Flask(__name__, instance_relative_config=True)
    api = Api(app)

    app.config.from_object(app_config[config_name])
    app.url_map.strict_slashes = False
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')

    jwt.init_app(app)

    from app.v1.views.users_view import Signup, Login
    from app.v1.views.products_view import Products
    from app.v1.views.products_view import ProductView

    api.add_resource(Signup, '/api/v1/user/signup')
    api.add_resource(Login, '/api/v1/user/login')
    api.add_resource(Products, '/api/v1/products')
    api.add_resource(ProductView, '/api/v1/products/<product_id>')

    return app
