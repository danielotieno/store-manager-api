"""
This model defines a category class and it's methods
It also create data structure to store category data

"""
import uuid
from datetime import datetime
from flask import request

from app.v2.database.conn import database_connection


class Category:
    """ Create a Category class to hold cetegories methods """

    def __init__(self):
        """ Initialize empty Category list and database connection"""
        self.conn = database_connection()
        self.conn.autocommit = True
        self.cur = self.conn.cursor()
        self.category_list = []
        self.category_details = {}

    def create_cetegory(self, category_name, category_status):
        """ A method to create categories """

        # check if category is already created
        self.cur.execute("SELECT * FROM categories_table WHERE category_name=%(category_name)s",
                         {'category_name': category_name})
        if self.cur.rowcount > 0:
            return {"message": "Category already exists."}, 400
        else:
            self.cur.execute(
                "INSERT INTO categories_table(category_name, category_status)\
            VALUES(%(category_name)s, %(category_status)s);", {
                    'category_name': category_name, 'category_status': category_status})
            self.conn.commit()
            return {"message": "Category added successfully"}, 201

    def modify_category(self, category_id, category_name, category_status):
        """ A method to modify category """
        self.cur.execute("SELECT * FROM categories_table WHERE category_id=%(category_id)s",
                         {'category_id': category_id})
        if self.cur.rowcount > 0:
            # update product details
            self.cur.execute(
                "UPDATE categories_table SET category_name=%s, category_status=%s\
            WHERE category_id=%s", (category_name, category_status, category_id))
            self.conn.commit()
            return {"message": "Successfully updated"}, 201
        return {"message": "Category Not Found."}, 400

    def delete_category(self, category_id):
        """ A method to delete category using category id """
        self.cur.execute("SELECT * FROM categories_table WHERE category_id=%(category_id)s",
                         {'category_id': category_id})
        if self.cur.rowcount > 0:
            # delete a category
            self.cur.execute(
                "DELETE FROM categories_table WHERE category_id=%(category_id)s", {
                    'category_id': category_id})
            self.conn.commit()
            return {
                "message": "Category deleted successfully"}, 201
        return {"message": "Category Not Found"}, 400
