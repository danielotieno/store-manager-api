import unittest
import json

from .start import BaseClass

from app.v1 import create_app

ADD_UPDATE_URL = '/api/v1/sales/3'
GET_SINGLE_URL = '/api/v1/sales/1'
GET_ALL_URL = '/api/v1/sales'
DELETE_URL = '/api/v1/sales/2'
MODIFY_URL = '/api/v1/sales/8'
SIGNUP_URL = '/api/v1/auth/signup'
LOGIN_URL = '/api/v1/auth/login'


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

        self.client.post(
            GET_ALL_URL,
            data=self.create_sale,
            content_type='application/json')

    def logged_in_user(self):
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

    def get_token(self):
        login_user = self.logged_in_user()
        token = login_user.get('token')

        return token

    # def test_add_sale(self):
    #     """ Test for sale order creation """
    #     access_token = self.get_token()
    #     print(access_token)

    #     resource = self.client.post(
    #         GET_ALL_URL,
    #         data=self.create_sale,
    #         content_type='application/json',
    #         headers={'Authorization': 'Bearer '+access_token})

    #     data = json.loads(resource.data.decode('utf-8'))
    #     print(data)
    #     self.assertEqual(resource.status_code, 201)
    #     self.assertEqual(resource.content_type, 'application/json')

    def test_get_all_sales(self):
        """ Test for getting all sales record """
        access_token = self.get_token()
        print(access_token)
        resource = self.client.get(
            GET_ALL_URL,
            data=json.dumps(dict()),
            content_type='application/json',
            headers={'Authorization': 'Bearer '+access_token})

        data = json.loads(resource.data.decode())
        print(data)
        self.assertEqual(resource.status_code, 200)
        self.assertEqual(resource.content_type, 'application/json')

    def test_get_specific_sale_by_id(self):
        """ Test for getting specific sale record by id """
        resource = self.client.get(GET_SINGLE_URL)
        self.assertEqual(resource.status_code, 404)
        self.assertEqual(resource.content_type, 'application/json')
