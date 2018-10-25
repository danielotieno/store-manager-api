import unittest
import json

from app.v2 import create_app
from app.v2.models.user import User, DB

from app.v2.database.conn import init_database, drop_all_tables

SIGNUP_URL = '/api/v2/auth/signup'
LOGIN_URL = '/api/v2/auth/login'


class BaseClass(unittest.TestCase):
    """This is the base class for test cases."""

    def setUp(self):
        """Initialize app and define test variables"""
        self.app = create_app("testing")
        self.client = self.app.test_client()
        with self.app.app_context():
            drop_all_tables()
            init_database()

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

        result = json.loads(res.data.decode('utf-8'))

        return result

    def get_token(self):
        login = self.logged_in_admin()
        token = login.get('token')

        return token

    def tearDown(self):
        '''Clears the database'''
        DB.drop()
