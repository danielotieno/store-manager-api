import unittest
import json

from .start import BaseClass

from app.v2 import create_app


SIGNUP_URL = '/api/v2/auth/signup'
LOGIN_URL = '/api/v2/auth/login'
GET_ALL_URL = '/api/v2/sales'
DELETE_URL = '/api/v2/sales/2'
MODIFY_URL = '/api/v2/sales/8'


class TestCategory(unittest.TestCase):
    """This is a category class for test cases."""

    def setUp(self):
        """Initialize app and define test variables"""
        self.app = create_app("testing")
        self.client = self.app.test_client()

        self.create_category = json.dumps(dict(
            category_id=1,
            name='Shirt',
            status='Active'))

        self.admin_data = {
            "username": "admin",
            "email": "admin@email.com",
            "password": "admin12345",
            "role": "Admin"

        }

        self.client.post(
            GET_ALL_URL,
            data=self.create_category,
            content_type='application/json')

    def logged_in_admin(self):
        """ Method to create and login admin """
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
        """ A method to get admin token """
        login = self.logged_in_admin()
        token = login.get('token')

        return token

    def test_add_product(self):
        """ Test to add category """

        resource = self.client.post(
            GET_ALL_URL,
            data=self.create_category,
            content_type='application/json')

        data = json.loads(resource.data.decode())
        print(data)
        self.assertEqual(resource.status_code, 201)
        self.assertEqual(resource.content_type, 'application/json')

    def test_modify_category(self):
        """ Test to modify category """
        response = self.client.post(GET_ALL_URL, data=self.create_category,
                                    content_type='application/json')

        data = json.loads(response.data.decode('utf-8'))
        print(data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.content_type, 'application/json')

        response = self.client.put(MODIFY_URL,
                                   data=json.dumps(dict(
                                       category_id=1,
                                       name='Shirt',
                                       status='Inactive')),
                                   content_type='application/json')
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data.decode('utf-8'))
        print(result)

    def test_delete_category(self):
        """ Test to delete a category """
        response = self.client.delete(
            DELETE_URL, data=json.dumps(dict(product_id=2,
                                             name='Shirt',
                                             status='Active')), content_type='application/json')
        self.assertEqual(response.status_code, 200)
