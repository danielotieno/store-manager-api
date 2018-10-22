from functools import wraps

from flask_restful import reqparse
from flask_jwt_extended import get_jwt_identity

from app.v1.models.user import User

import re


def admin_required(f):
    ''' Restrict access if not admin '''
    @wraps(f)
    def wrapper_function(*args, **kwargs):
        user = User.get_user_by_role(get_jwt_identity()['role'])

        if not user.role == 'Admin':
            return {'message': 'Anauthorized access, you must be an admin to access this level'}, 401
        return f(*args, **kwargs)
    return wrapper_function


def store_attendant_required(f):
    ''' A decorator for store attendant '''
    @wraps(f)
    def wrapper_function(*args, **kwargs):
        user = User.get_user_by_role(get_jwt_identity()['role'])

        if not user.role == 'Store_Attendant':
            return {'message': 'Anauthorized access, you must be a Store Attendant to access this level'}, 401
        return f(*args, **kwargs)
    return wrapper_function


def required(var):
    """checks if any required field is blank"""
    if var.strip() == '':
        return 'All fields are required'
    return None


def validate_data(data):
    """validate product details"""
    try:
        # check if there are specil characters in the username
        if not re.match("^[a-zA-Z0-9_ ]+$", data['name'].strip()):
            return "product name can only contain characters"

        # check if the name contains only numbers or underscore
        elif not re.match("^[a-zA-Z0-9_ ]+$", data['description'].strip()):
            return "description can only contain characters"

        # Check if category contains aplhanumeric characters
        elif not re.match("^[a-zA-Z0-9_ ]+$", data['category'].strip()):
            return "category can only contain alphanumeric characters"
        else:
            return "valid"
    except Exception as error:
        return "please provide all the fields, missing " + str(error)
