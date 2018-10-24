import unittest
import json

from .start import BaseClass

from app.v2 import create_app

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

        self.create_sale = json.dumps(dict(
            sale_id=1,
            customer='Daniel Otieno',
            product='Polo Shirt',
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

    def test_add_sale(self):
        """ Test for sale order creation """
        access_token = self.login_user()

        resource = self.client.post(
            GET_ALL_URL,
            data=self.create_sale,
            content_type='application/json',
            headers={'Authorization': 'Bearer '+access_token})

        data = json.loads(resource.data.decode('utf-8'))
        self.assertEqual(resource.status_code, 201)
        self.assertEqual(resource.content_type, 'application/json')
        self.assertEqual(data["message"], "Sale Order successfully created")

    def test_get_all_sales(self):
        """ Test for getting all sales record """
        access_token = self.get_admin_token()
        resource = self.client.get(
            GET_ALL_URL,
            data=json.dumps(dict()),
            content_type='application/json',
            headers={'Authorization': 'Bearer '+access_token})

        data = json.loads(resource.data.decode())
        self.assertEqual(resource.status_code, 200)
        self.assertEqual(resource.content_type, 'application/json')
        self.assertEqual(data["message"], "Successfully")

    def test_get_specific_sale_by_id(self):
        """ Test for getting specific sale record by id """
        resource = self.client.get(GET_SINGLE_URL)
        self.assertEqual(resource.status_code, 404)
        self.assertEqual(resource.content_type, 'application/json')
