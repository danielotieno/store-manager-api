from flask import Flask, request
from flask_restful import Resource

from app.v1.models.sale_order import Sale
from utlis.salereq import validate_data

saleObject = Sale()


class Sales(Resource):
    """
    Resource for creating a new sale order
    """

    def post(self):
        """ Add a new sale order endpoint """

        data = request.get_json()
        res = validate_data(data)

        if res == "valid":
            customer = data['customer']
            product = data['product']
            quantity = data['quantity']
            created_by = data['created_by']
            total_amount = data['total_amount']

            res = saleObject.create_sale(
                customer, product, quantity, created_by, total_amount)

            return res
        return {"message": res}, 400
