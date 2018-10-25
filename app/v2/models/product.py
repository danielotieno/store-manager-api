"""
This model defines a product class and it's methods
It also create data structure to store product data

"""
import uuid
from datetime import datetime
from flask import request

from app.v2.database.conn import database_connection


class Product:
    """ Create a Product class to hold product methods """

    def __init__(self):
        """ Initialize empty Product list"""
        self.conn = database_connection()
        self.conn.autocommit = True
        self.cur = self.conn.cursor()
        self.product_list = []
        self.product_details = {}

    def create_product(self, product_name, product_description, price, category, quantity, low_inventory):
        """Create product item"""
        # check if product is already created
        self.cur.execute("SELECT * FROM products_table WHERE product_name=%(product_name)s",
                         {'product_name': product_name})
        if self.cur.rowcount > 0:
            return {"message": "Product already exists."}, 400
        else:
            self.cur.execute(
                "INSERT INTO products_table(product_name,product_description,price,category,quantity,low_inventory)\
            VALUES(%(product_name)s, %(product_description)s, %(price)s, %(category)s, %(quantity)s, %(low_inventory)s);", {
                    'product_name': product_name, 'product_description': product_description, 'price': price, 'category': category, 'quantity': quantity, 'low_inventory': low_inventory})
            self.conn.commit()
            return {"message": "Product added successfully"}, 201

    def get_products(self):
        """ A method to get all products """
        self.cur.execute("SELECT * FROM products_table")
        if self.cur.rowcount > 0:
            rows = self.cur.fetchall()
            self.product_list = []
            for product in rows:
                self.product_details.update({
                    'product_id': product[0],
                    'product_name': product[1],
                    'product_description': product[2],
                    'price': product[3],
                    'category': product[4],
                    'quantity': product[5],
                    'low_inventory': product[4]})
                self.product_list.append(dict(self.product_details))
            return {
                "message": "Successfully. Product Found",
                "Products": self.product_list}, 200
        return {
            "message": "No Product.", "status": "Ok"}, 200

    def get_product_by_id(self, product_id):
        """ A method to get a single product """
        # The function filter function offers an elegant way to filter out all the elements of a list.
        product = next(
            filter(lambda x: x['product_id'] == product_id, self.product_list), None)
        return {'Product': product}, 200 if product else 404

    def update_a_product(self, product_id):
        """ A method to update a product """
        data = request.get_json()
        product = next(
            filter(lambda x: x['product_id'] == product_id, self.product_list), None)

        if product is None:
            product = {
                'name': data['name'],
                'description': data['description'],
                'price': float(data['price']),
                'category': data['category'],
                'quantity': int(data['quantity']),
                'low_inventory': int(data['low_inventory'])
            }
            self.product_list.append(product), 201
        else:
            product.update(product)
        return {'Product': product, 'message': 'Successfully updated'}, 200

    def delete_a_product(self, product_id):
        """ A method to delete a product using product id """
        self.product_list
        self.product_list = list(
            filter(lambda x: x['product_id'] != product_id, self.product_list))
        return {'message': 'Product deleted successfully'}, 200
