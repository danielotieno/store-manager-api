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
        self.cur.execute("SELECT * FROM sales_table")
        if self.cur.rowcount > 0:
            rows = self.cur.fetchall()
            self.sales_list = []
            for sale in rows:
                self.sales_details.update({
                    'sale_id': sale[0],
                    'customer': sale[1],
                    'product': sale[2],
                    'quantity': sale[3],
                    'created_by': sale[4],
                    'total_amount': sale[5]})
                self.sales_list.append(dict(self.sales_details))
            return {
                "message": "Successfully",
                "Products": self.sales_details}, 200
        return {
            "message": "Sales Not Found"}, 200

    def get_sale_record_by_id(self, sale_id):
        """ A method to get a single sale record """
        sale = next(
            filter(lambda x: x['sale_id'] == sale_id, self.sales_list), None)
        return {'Sale Record': sale}, 200 if sale else 404
