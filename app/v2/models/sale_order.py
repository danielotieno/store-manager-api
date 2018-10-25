"""
This model defines a sales order class and it's methods
It also create data structure to store sales order data

"""
import uuid
from datetime import datetime

from app.v2.database.conn import database_connection


class Sale:
    """ Create a Sale class to hold sales methods """

    def __init__(self):
        """ Initialize sales database table """
        self.conn = database_connection()
        self.conn.autocommit = True
        self.cur = self.conn.cursor()
        self.sales_list = []
        self.sales_details = {}

    def create_sale(self, customer, product, quantity, created_by, total_amount):
        """Create sale item in table"""
        self.cur.execute(
            "INSERT INTO sales_table(customer, product, quantity, created_by, total_amount)\
        VALUES(%(customer)s, %(product)s, %(quantity)s, %(created_by)s, %(total_amount)s);", {
                'customer': customer, 'product': product, 'quantity': quantity, 'created_by': created_by, 'total_amount': total_amount})
        self.conn.commit()
        return {"message": "Sale Order successfully created"}, 201

    def get_sales(self):
        """ A method to get all sales record """
        return {'Sales Record': self.sales_list, 'message': 'Successfully'}, 200

    def get_sale_record_by_id(self, sale_id):
        """ A method to get a single sale record """
        sale = next(
            filter(lambda x: x['sale_id'] == sale_id, self.sales_list), None)
        return {'Sale Record': sale}, 200 if sale else 404
