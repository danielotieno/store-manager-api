import unittest
import json

from app.v2 import create_app
from app.v2.database.conn import init_database, drop_all_tables


ADD_UPDATE_URL = '/api/v2/sales/3'
GET_SINGLE_URL = '/api/v2/sales/1'
GET_ALL_URL = '/api/v2/sales'
DELETE_URL = '/api/v2/sales/2'
MODIFY_URL = '/api/v2/sales/8'
SIGNUP_URL = '/api/v2/auth/signup'
LOGIN_URL = '/api/v2/auth/login'


class TestSale(unittest.TestCase):
    """This is the sale class for test cases."""

    def setUp(self):
        """Initialize app and define test variables"""
        self.app = create_app("testing")
        self.client = self.app.test_client()
        with self.app.app_context():
            init_database()

        self.create_product = json.dumps(dict(
            product_name='Shirt',
            description='Cool Polo shirt',
            price=500,
            category='Polo',
            quantity=5,
            low_inventory=10))

        self.create_sale = json.dumps(dict(
            customer='Daniel Otieno',
            product_name='Polo Shirt',
            quantity=5,
            created_by='Store Attendant',
            total_amount=3000
        ))

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
            "role": "Store_Attendant"
        }

        self.client.post(
            GET_ALL_URL,
            data=self.create_sale,
            content_type='application/json')

    def logged_in_admin(self):
        # first create user
        self.client.post(SIGNUP_URL,
                         data=json.dumps(self.admin_data), content_type='application/json')

        # then log in user
        res = self.client.post(LOGIN_URL,
                               data=json.dumps(
                                   self.admin_data),
                               content_type='application/json')

        result = json.loads(res.data.decode('utf-8'))

        return result

    def get_admin_token(self):
        login_admin = self.logged_in_admin()
        token = login_admin.get('token')

        return token

    def login_user(self):
        token = self.get_admin_token()

        self.client.post(SIGNUP_URL,
                         data=json.dumps(self.user_data), content_type='application/json',
                         headers={'Authorization': 'Bearer '+token})

        res = self.client.post(LOGIN_URL,
                               data=json.dumps(
                                   self.user_data),
                               content_type='application/json')

        result = json.loads(res.data.decode('utf-8'))

        return result['token']

    def tearDown(self):
        """Teardown all the test data"""
        with self.app.app_context():
            drop_all_tables()


if __name__ == '__main__':
    unittest.main()
