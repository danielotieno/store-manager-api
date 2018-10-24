"""
This model defines a category class and it's methods
It also create data structure to store category data

"""
import uuid
from datetime import datetime
from flask import request
from flask import current_app


class Category:
    """ Create a Category class to hold cetegories methods """

    def __init__(self):
        """ Initialize empty Category list"""
        self.category_list = []

    def create_cetegory(self, name, status):
        """ A method to create categories """

        self.category_details = {}

        self.category_details['cetegory_id'] = str(uuid.uuid1())
        self.category_details['name'] = name
        self.category_details['status'] = status
        self.category_details['date'] = str(datetime.now().replace(
            second=0, microsecond=0))
        self.category_list.append(self.category_details)
        return {'Categories': self.category_list, 'message': 'Category added successfully'}, 201
