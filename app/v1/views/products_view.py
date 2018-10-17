from flask import Flask, request
from flask_restful import Resource, reqparse

from app.v1.models.product import Product
from utlis.required import validate_data

productObject = Product()


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

            res = productObject.create_product(
                name, description, price, category, quantity, low_inventory)

            return res
        return {"message": res}, 400

    def get(self):
        get_all = productObject.get_products()
        return get_all
