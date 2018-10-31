import unittest
import json

from app.v2 import create_app

from app.v2.database.conn import init_database, drop_all_tables

ADD_UPDATE_URL = '/api/v2/products/3'
GET_SINGLE_URL = '/api/v2/products/1'
GET_ALL_URL = '/api/v2/products'
DELETE_URL = '/api/v2/products/2'
SIGNUP_URL = '/api/v2/auth/signup'
LOGIN_URL = '/api/v2/auth/login'


class TestProduct(unittest.TestCase):
    """This is the product class for test cases."""

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

    def create_default_product(self):
        """ Create default prdouct """
        access_token = self.get_token()
        self.client.post(
            GET_ALL_URL,
            data=self.create_product,
            content_type='application/json',
            headers={'Authorization': 'Bearer '+access_token})

    def test_add_product(self):
        """ Test for product creation """
        access_token = self.get_token()
        resource = self.client.post(
            GET_ALL_URL,
            data=self.create_product,
            content_type='application/json',
            headers={'Authorization': 'Bearer '+access_token})

        data = json.loads(resource.data.decode())
        self.assertEqual(data["message"], "Product added successfully")
        self.assertEqual(resource.status_code, 201)
        self.assertEqual(resource.content_type, 'application/json')

    def test_get_all_products(self):
        """ Test for getting all products """
        self.create_default_product()
        resource = self.client.get(
            GET_ALL_URL,
            content_type='application/json')

        data = json.loads(resource.data.decode())
        self.assertEqual(resource.status_code, 200)
        self.assertEqual(resource.content_type, 'application/json')
        self.assertEqual(data["message"], "Successfully. Product Found")

    def test_get_specific_product_by_id(self):
        """ Test for getting specific product by id """
        self.create_default_product()
        resource = self.client.get(GET_SINGLE_URL)
        self.assertEqual(resource.status_code, 200)
        self.assertEqual(resource.content_type, 'application/json')

    def test_update_a_product(self):
        """ Test to modify a product """
        access_token = self.get_token()
        self.create_default_product()
        response = self.client.put(GET_SINGLE_URL,
                                   data=json.dumps(dict(
                                       product_id=1,
                                       product_name='Suit',
                                       description='Cool leather suit',
                                       price=1000,
                                       category='Polo',
                                       quantity=5,
                                       low_inventory=10)),
                                   content_type='application/json',
                                   headers={'Authorization': 'Bearer '+access_token})
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result["message"], "Successfully updated")
        self.assertEqual(response.status_code, 201)

    def test_delete_a_product(self):
        """ Test to delete a product """
        access_token = self.get_token()
        response = self.client.delete(
            DELETE_URL, data=json.dumps(dict(product_id=2,
                                             product_name='Shirt',
                                             description='Cool Polo shirt',
                                             price=500,
                                             category='Polo',
                                             quantity=5,
                                             low_inventory=10)), content_type='application/json',
            headers={'Authorization': 'Bearer '+access_token})
        self.assertEqual(response.status_code, 400)

    def tearDown(self):
        """Teardown all the test data"""
        with self.app.app_context():
            drop_all_tables()


if __name__ == '__main__':
    unittest.main()
