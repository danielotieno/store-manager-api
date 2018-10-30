""" Validations fields for sales """
import re


def validate_data(data):
    """validate sales details when posting"""
    try:
        # check if there are specil characters in the username
        if not re.match("^[a-zA-Z0-9_ ]+$", data['customer'].strip()):
            return "product name can only contain characters"

        # check if the name contains only numbers or underscore
        elif not re.match("^[a-zA-Z0-9_ ]+$", data['product_name'].strip()):
            return "description can only contain characters"

        # Check if category contains aplhanumeric characters
        elif not re.match("^[a-zA-Z0-9_ ]+$", data['created_by'].strip()):
            return "createdby can only contain alphanumeric characters"
        else:
            return "valid"
    except Exception as error:
        return "please provide all the fields, missing " + str(error)
