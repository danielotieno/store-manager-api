import unittest
import json

from app.v1 import create_app

ADD_UPDATE_URL = '/api/v1/products/3'
GET_SINGLE_URL = '/api/v1/products/1'
GET_ALL_URL = '/api/v1/products'
DELETE_URL = '/api/v1/products/2'
MODIFY_URL = '/api/v1/products/8'


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

        self.client.post(
            GET_ALL_URL,
            data=self.create_product,
            content_type='application/json')

    # def test_add_product(self):
    #     """ Test for product creation """

    #     resource = self.client.post(
    #         GET_ALL_URL,
    #         data=self.create_product,
    #         content_type='application/json')

    #     data = json.loads(resource.data.decode())
    #     print(data)
    #     self.assertEqual(resource.status_code, 201)
    #     self.assertEqual(resource.content_type, 'application/json')

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
