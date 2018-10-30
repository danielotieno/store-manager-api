import unittest
import json

from app.v2 import create_app

from app.v2.database.conn import init_database, drop_all_tables


SIGNUP_URL = '/api/v2/auth/signup'
LOGIN_URL = '/api/v2/auth/login'
GET_ALL_URL = '/api/v2/categories'
DELETE_URL = '/api/v2/categories/2'
MODIFY_URL = '/api/v2/categories/1'


class TestCategory(unittest.TestCase):
    """This is a category class for test cases."""

    def setUp(self):
        """Initialize app and define test variables"""
        self.app = create_app("testing")
        self.client = self.app.test_client()
        with self.app.app_context():
            init_database()

        self.create_category = json.dumps(dict(
            category_id=1,
            name='TestCategory',
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

    def test_add_category(self):
        """ Test to add category """
        access_token = self.get_token()
        resource = self.client.post(
            GET_ALL_URL,
            data=self.create_category,
            content_type='application/json',
            headers={'Authorization': 'Bearer '+access_token})

        data = json.loads(resource.data.decode())
        print(data)
        self.assertEqual(resource.status_code, 201)
        self.assertEqual(resource.content_type, 'application/json')
        self.assertEqual(data["message"], "Category added successfully")

    def test_delete_category(self):
        """ Test to delete a category """
        access_token = self.get_token()
        response = self.client.delete(
            DELETE_URL, data=json.dumps(dict(category_id=2,
                                             name='Shirt',
                                             status='Active')), content_type='application/json',
            headers={'Authorization': 'Bearer '+access_token})
        self.assertEqual(response.status_code, 400)

    def tearDown(self):
        """Teardown all the test data"""
        with self.app.app_context():
            drop_all_tables()
