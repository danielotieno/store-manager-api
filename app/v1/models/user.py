"""
This model defines a user class and it's methods
It also create data structure to store user data

"""

import re
import uuid
from datetime import date, datetime, timedelta

user_list = []


class User:
    """ A class to handle activities related to a user """

    def validate_data(self, username, email, password, confirm_password):
        """ A method to validate username and password details """
        if not re.match("^[a-zA-Z0-9_]*$", username)\
                or not re.match("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
            return "Username or email can only contain alphanumeric characters"
        elif len(username.strip()) < 4:
            return "Your username should be atleast four characters long"
        elif len(password) < 8:
            return "Your password should be atleast eight characters long"
        elif password != confirm_password:
            return "Your passwords must match"
        else:
            return True

    def __init__(self, username, email, password, role):
        """ A constructor method for creating a user """
        self.id = uuid.uuid1()
        self.username = username
        self.email = email
        self.password = password
        self.role = "Store Attendant"
