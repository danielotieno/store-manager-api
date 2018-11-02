""" Validations fields for sales """
import re


def validate_data(data):
    """validate sales details when posting"""
    try:
        # check if there are specil characters in the username
        if not isinstance(data['cart'], list):
            return "cart can only contain a list"
        else:
            return "valid"
    except Exception as error:
        return "please provide all the fields, missing " + str(error)


def validate_cart(data):
    """validate sales details when posting"""
    try:
        # check if there are specil characters in the username
        if not isinstance(data['product_id'], int):
            return "Product Id shoul be an integer"
        else:
            return "valid"
    except Exception as error:
        return "please provide all the fields, missing " + str(error)
