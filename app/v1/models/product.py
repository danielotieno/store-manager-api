"""
This model defines a product class and it's methods
It also create data structure to store product data

"""
import uuid
from datetime import datetime
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
        return {'Products': self.product_list, 'message': 'Successfully'}, 200

    def get_product_by_id(self, product_id):
        """ A method to get a single product """

        # The function filter function offers an elegant way to filter out all the elements of a list.
        product = next(
            filter(lambda x: x['product_id'] == product_id, self.product_list), None)
        return {'Product': product}, 200 if product else 404
