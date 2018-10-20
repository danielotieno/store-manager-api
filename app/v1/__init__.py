""" This is the file that start our application and contains api endpoints """
import os

from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager

from app.v1.models.user import User

import config

JWT = JWTManager()


def create_app(config_name):
    """Function to create a flask app depending on the configuration passed"""

    app = Flask(__name__)
    api = Api(app)

    app.config.from_object('config')
    app.url_map.strict_slashes = False
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')

    JWT.init_app(app)

    user = User(os.getenv('ADMIN_USERNAME'), os.getenv(
        'ADMIN_EMAIL'), os.getenv('ADMIN_PASSWORD'), os.getenv('ADMIN_ROLE'))
    user = user.save()

    from app.v1.views.welcome import Welcome
    from app.v1.views.users_view import Signup, Login
    from app.v1.views.products_view import Products
    from app.v1.views.products_view import ProductView
    from app.v1.views.sales_view import Sales
    from app.v1.views.sales_view import SaleView

    api.add_resource(Welcome, '/')
    api.add_resource(Signup, '/api/v1/auth/signup')
    api.add_resource(Login, '/api/v1/auth/login')
    api.add_resource(Products, '/api/v1/products')
    api.add_resource(ProductView, '/api/v1/products/<product_id>')
    api.add_resource(Sales, '/api/v1/sales')
    api.add_resource(SaleView, '/api/v1/sales/<sale_id>')

    return app
