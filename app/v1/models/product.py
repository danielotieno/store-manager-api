"""
This model defines a product class and it's methods
It also create data structure to store product data

"""
import uuid
from datetime import date, datetime
from flask import request
from flask import current_app


class Product:
    """ Create a Product class to hold product methods """

    def __init__(self):
        """ Initialize empty Product list"""
        self.product_list = []

    def create_product(self, name, description, price, category, quantity, low_inventory):
        """Create product item"""

        self.product_details = {}

        self.product_details['product_id'] = str(uuid.uuid1())
        self.product_details['name'] = name
        self.product_details['description'] = description
        self.product_details['price'] = price
        self.product_details['category'] = category
        self.product_details['quantity'] = quantity
        self.product_details['low_inventory'] = low_inventory
        self.product_details['date'] = str(datetime.now().replace(
            second=0, microsecond=0))
        self.product_list.append(self.product_details)
        return {'Products': self.product_list, 'message': 'Product added successfully'}, 201

    def get_products(self):
        """ A method to get all products """
        return self.product_list, 200

    def get_product_by_id(self, product_id):
        """ A method to get a single product """
        product = next(
            filter(lambda x: x['product_id'] == product_id, self.product_list), None)
        return {'Product': product}, 200 if product else 404

    def update_a_product(self, product_id):
        """ A method to update a specific product """
        data = request.get_json()
        product = next(
            filter(lambda x: x['product_id'] == product_id, self.product_list), None)

        if product is None:
            product = {
                'name': data['name']
            }
            self.product_list.append(product), 201
        else:
            product.update(product), 200
        return product

    def delete_a_product(self, product_id):
        """ A method to delete a single product using product id """
        self.product_list
        self.product_list = list(
            filter(lambda x: x['product_id'] != product_id, self.product_list))
        return {'message': 'Product deleted successfully'}, 200
