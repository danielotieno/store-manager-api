"""
This model defines a sales order class and it's methods
It also create data structure to store sales order data

"""
import uuid
from datetime import date, datetime
from flask import current_app


class Sale:
    """ Create a Sale class to hold sales methods """

    def __init__(self):
        """ Initialize empty Sales list"""
        self.sales_list = []

    def create_sale(self, customer, product, quantity, created_by, total_amount):
        """Create sale item"""

        self.sales_details = {}

        self.sales_details['sale_id'] = str(uuid.uuid1())
        self.sales_details['customer'] = customer
        self.sales_details['product'] = product
        self.sales_details['quantity'] = quantity
        self.sales_details['created_by'] = created_by
        self.sales_details['total_amount'] = total_amount
        self.sales_details['sales_date'] = str(datetime.now().replace(
            second=0, microsecond=0))
        self.sales_list.append(self.sales_details)
        return {'Sale Orders': self.sales_list, 'message': 'Sale Order successfully created'}, 201

    def get_sales(self):
        """ A method to get all sales record """
        return {'Sales Record': self.sales_list, 'message': 'Successfully'}, 200

    def get_sale_record_by_id(self, sale_id):
        """ A method to get a single sale record """
        sale = next(
            filter(lambda x: x['sale_id'] == sale_id, self.sales_list), None)
        return {'Sale Record': sale}, 200 if sale else 404
