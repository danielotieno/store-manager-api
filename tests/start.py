import unittest
import json

from app.v1 import create_app
from app.v1.models.user import User, DB

SIGNUP_URL = '/api/v1/auth/signup'
LOGIN_URL = '/api/v1/auth/login'


class BaseClass(unittest.TestCase):
    """This is the base class for test cases."""

    def setUp(self):
        """Initialize app and define test variables"""
        self.app = create_app("testing")
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

        self.admin_data = {
            "username": "admin",
            "email": "admin@email.com",
            "password": "admin12345",
            "role": "Admin"

        }

        self.user_data = {
            "username": "danny",
            "email": "danny@gmail.com",
            "password": "password1",
            "role": "Store Attendant"
        }

        self.user1 = User(
            username="testuser",
            email="testuser@email.com",
            password="password",
            role="Store Attendant")

        self.test_user = User(
            username='dannyke',
            email='danny@mail.com',
            password='password2',
            role="Store Attendant")

    def logged_in_user(self):
        # first create user
        self.client.post(SIGNUP_URL,
                         data=json.dumps(self.user_data), content_type='application/json')

        # then log in user
        res = self.client.post(LOGIN_URL,
                               data=json.dumps(
                                   {'email': 'danny@gmail.com', 'password': 'password1'}),
                               content_type='application/json')

        return res

    def logged_in_admin(self):
        # first create admin
        self.client.post(SIGNUP_URL,
                         data=json.dumps(self.admin_data), content_type='application/json')

        # then log in admin
        res = self.client.post(LOGIN_URL,
                               data=json.dumps(
                                   self.admin_data),
                               content_type='application/json')

        return res

    def tearDown(self):
        '''Clears the database'''
        DB.drop()
