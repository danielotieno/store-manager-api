""" This is a resource view for products """
from flask import request
from flask_restful import Resource

from app.v1.models.product import Product
from utlis.required import validate_data

PRODUCT_OBJECT = Product()


class Products(Resource):
    """
    Resource for creating a new product
    """

    def post(self):
        """ Add a new product endpoint """

        data = request.get_json()
        res = validate_data(data)

        if res == "valid":
            name = data['name']
            description = data['description']
            price = data['price']
            category = data['category']
            quantity = data['quantity']
            low_inventory = data['low_inventory']

            res = PRODUCT_OBJECT.create_product(
                name, description, price, category, quantity, low_inventory)

            return res
        return {"message": res}, 400

    def get(self):
        """ A method to get all products """
        get_all = PRODUCT_OBJECT.get_products()
        return get_all


class ProductView(Resource):
    """
    Resource for product endpoints with ids
    """

    def get(self, product_id):
        """ Get a specific product method """
        get_product = PRODUCT_OBJECT.get_product_by_id(product_id)
        return get_product
