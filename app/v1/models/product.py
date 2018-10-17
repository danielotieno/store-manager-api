"""
This model defines a product class and it's methods
It also create data structure to store product data

"""
import uuid
from datetime import datetime, timedelta
from flask import request
from flask import current_app


class Product:
    """ Create a Product class to hold product methods """

    def __init__(self):
        """ Initialize empty Product list"""
        self.product_list = []

    def create_product(self, name, description, price, category, low_inventory):
        """Create product item"""

        self.product_details = {}

        self.id = uuid.uuid1()
        self.product_details['name'] = name
        self.product_details['description'] = description
        self.product_details['price'] = price
        self.product_details['category'] = category
        self.product_details['low_inventory'] = low_inventory
        self.product_list.append(self.product_details)
        return self.product_list, 201
