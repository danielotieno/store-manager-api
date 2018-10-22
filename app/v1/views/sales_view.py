""" A resource view for sales endpoints """
from flask import request
from flask_restful import Resource

from flask_jwt_extended import jwt_required

from app.v1.models.sale_order import Sale
from utlis.salereq import validate_data
from utlis.required import admin_only, store_attendant_required

SALE_OBJECT = Sale()


class Sales(Resource):
    """
    Resource for creating a new sale order
    """

    @jwt_required
    @store_attendant_required
    def post(self):
        """ Add a new sale order endpoint """

        data = request.get_json()
        res = validate_data(data)

        if res == "valid":
            customer = data['customer']
            product = data['product']
            quantity = int(data['quantity'])
            created_by = data['created_by']
            total_amount = int(data['total_amount'])

            res = SALE_OBJECT.create_sale(
                customer, product, quantity, created_by, total_amount)

            return res
        return {"message": res}, 400

    @jwt_required
    @admin_only
    def get(self):
        """ A method to get all sales record """
        get_record = SALE_OBJECT.get_sales()
        return get_record


class SaleView(Resource):
    """
    Resource for sales endpoints with ids
    """

    def get(self, sale_id):
        """ Get a specific sale record method """
        get_sale = SALE_OBJECT.get_sale_record_by_id(sale_id)
        return get_sale
