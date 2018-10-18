from flask import current_app


class Admin:
    """ Create a Product class to hold product methods """

    def __init__(self):
        """ Initialize empty Product list"""
        self.admin_list = []

    def create_admin(self, username, email, password, role):
        """Create a default admin user"""

        self.admin_details = {}

        self.admin_details['username'] = username
        self.admin_details['email'] = email
        self.admin_details['password'] = password
        self.admin_details['role'] = role
        self.admin_list.append(self.admin_details)
