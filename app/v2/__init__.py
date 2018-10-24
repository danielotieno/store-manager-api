""" This is the file that start our application and contains api endpoints """
import os

from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager

from app.v2.models.user import User
from app.v2.views.users_view import BLACKLIST
from app.v2.database.conn import init_database

import config

JWT = JWTManager()


def create_app(config_name):
    """The create_app function wraps the creation of a new Flask object."""

    app = Flask(__name__)
    api = Api(app)

    app.config.from_object('config')
    app.url_map.strict_slashes = False
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
    app.config['JWT_BLACKLIST_ENABLED'] = True
    app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access']

    JWT.init_app(app)

    @JWT.token_in_blacklist_loader
    def check_if_token_blacklist(decrypted_token):
        '''check if jti(unique identifier) is in black list'''
        jti = decrypted_token['jti']
        return jti in BLACKLIST

    init_database()

    from app.v2.views.welcome import Welcome
    from app.v2.views.users_view import Signup, Login, Logout
    from app.v2.views.products_view import Products
    from app.v2.views.products_view import ProductView
    from app.v2.views.sales_view import Sales
    from app.v2.views.sales_view import SaleView
    from app.v2.views.categories_view import Categories
    from app.v2.views.categories_view import CategoryView

    api.add_resource(Welcome, '/')
    api.add_resource(Signup, '/api/v2/auth/signup')
    api.add_resource(Login, '/api/v2/auth/login')
    api.add_resource(Logout, '/api/v2/auth/logout')
    api.add_resource(Products, '/api/v2/products')
    api.add_resource(ProductView, '/api/v2/products/<product_id>')
    api.add_resource(Sales, '/api/v2/sales')
    api.add_resource(SaleView, '/api/v2/sales/<sale_id>')
    api.add_resource(Categories, '/api/v2/categories')
    api.add_resource(CategoryView, '/api/v2/categories/<category_id>')

    return app
