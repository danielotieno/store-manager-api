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
