""" This is a resource view for Category """
from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from app.v2.models.category import Category
from utlis.required import category_data, admin_required

CATEGORY_OBJECT = Category()


class Categories(Resource):
    """Resource for creating a category """

    @jwt_required
    @admin_required
    def post(self):
        """ Add a new category """

        data = request.get_json()
        res = category_data(data)

        if res == "valid":
            name = data['name']
            status = data['status']

            res = CATEGORY_OBJECT.create_cetegory(name, status)

            return res
        return {"message": res}, 400


class CategoryView(Resource):
    """ Resource for categories endpoints """

    @jwt_required
    @admin_required
    def put(self, category_id):
        """ A method for modifying category """
        data = request.get_json()
        res = category_data(data)

        if res == "valid":
            category_name = data['name']
            category_status = data['status']
        update_category = CATEGORY_OBJECT.modify_category(
            category_id, category_name, category_status)
        return update_category

    @jwt_required
    @admin_required
    def delete(self, category_id):
        """ A method to Delete a specific category """
        delete_category = CATEGORY_OBJECT.delete_category(category_id)
        return delete_category
