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

    def modify_category(self, category_id):
        """ A method to modify category """
        data = request.get_json()
        category = next(
            filter(lambda x: x['category_id'] == category_id, self.category_list), None)

        if category is None:
            category = {
                'name': data['name'],
                'status': data['status'],

            }
            self.category_list.append(category), 201
        else:
            category.update(category)
        return {'Category': category, 'message': 'Successfully updated'}, 200

    def delete_category(self, category_id):
        """ A method to delete category using category id """
        self.category_list
        self.category_list = list(
            filter(lambda x: x['category_id'] != category_id, self.category_list))
        return {'message': 'Category deleted successfully'}, 200
