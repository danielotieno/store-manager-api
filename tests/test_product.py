import unittest
import json

from .start import BaseClass

from app.v1 import create_app

ADD_UPDATE_URL = '/api/v1/products/3'
GET_SINGLE_URL = '/api/v1/products/1'
GET_ALL_URL = '/api/v1/products'
DELETE_URL = '/api/v1/products/2'
MODIFY_URL = '/api/v1/products/8'
SIGNUP_URL = '/api/v1/auth/signup'
LOGIN_URL = '/api/v1/auth/login'


class TestProduct(unittest.TestCase):
    """This is the product class for test cases."""

    def setUp(self):
        """Initialize app and define test variables"""
        self.app = create_app("testing")
        self.client = self.app.test_client()

        self.create_product = json.dumps(dict(
            product_id=1,
            name='Shirt',
            description='Cool Polo shirt',
            price=500,
            category='Polo',
            quantity=5,
            low_inventory=10))

        self.admin_data = {
            "username": "admin",
            "email": "admin@email.com",
            "password": "admin12345",
            "role": "Admin"

        }

        self.client.post(
            GET_ALL_URL,
            data=self.create_product,
            content_type='application/json')

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

    def test_add_product(self):
        """ Test for product creation """
        access_token = self.get_token()

        resource = self.client.post(
            GET_ALL_URL,
            data=self.create_product,
            content_type='application/json',
            headers={'Authorization': 'Bearer '+access_token})

        data = json.loads(resource.data.decode())
        print(data)
        self.assertEqual(resource.status_code, 201)
        self.assertEqual(resource.content_type, 'application/json')

    def test_get_all_products(self):
        """ Test for getting all products """
        resource = self.client.get(
            GET_ALL_URL,
            data=json.dumps(dict()),
            content_type='application/json')

        data = json.loads(resource.data.decode())
        print(data)
        self.assertEqual(resource.status_code, 200)
        self.assertEqual(resource.content_type, 'application/json')

    def test_get_specific_product_by_id(self):
        """ Test for getting specific product by id """
        resource = self.client.get(GET_SINGLE_URL)
        self.assertEqual(resource.status_code, 404)
        self.assertEqual(resource.content_type, 'application/json')


if __name__ == '__main__':
    unittest.main()
