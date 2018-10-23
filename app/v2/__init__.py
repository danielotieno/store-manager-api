""" This is the file that start our application and contains api endpoints """
import os

from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager

from app.v2.models.user import User

import config

JWT = JWTManager()


def create_app(config_name):
    """The create_app function wraps the creation of a new Flask object."""

    app = Flask(__name__)
    api = Api(app)

    app.config.from_object('config')
    app.url_map.strict_slashes = False
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')

    JWT.init_app(app)

    user = User('admin', 'admin@email.com', 'admin12345', 'Admin')
    user = user.save()

    from app.v2.views.welcome import Welcome
    from app.v2.views.users_view import Signup, Login
    from app.v2.views.products_view import Products
    from app.v2.views.products_view import ProductView
    from app.v2.views.sales_view import Sales
    from app.v2.views.sales_view import SaleView

    api.add_resource(Welcome, '/')
    api.add_resource(Signup, '/api/v2/auth/signup')
    api.add_resource(Login, '/api/v2/auth/login')
    api.add_resource(Products, '/api/v2/products')
    api.add_resource(ProductView, '/api/v2/products/<product_id>')
    api.add_resource(Sales, '/api/v2/sales')
    api.add_resource(SaleView, '/api/v2/sales/<sale_id>')

    return app
