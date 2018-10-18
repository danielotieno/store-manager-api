import unittest
import json

from app.v1 import create_app

ADD_UPDATE_URL = '/api/v1/sales/3'
GET_SINGLE_URL = '/api/v1/sales/1'
GET_ALL_URL = '/api/v1/sales'
DELETE_URL = '/api/v1/sales/2'
MODIFY_URL = '/api/v1/sales/8'


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

        self.client.post(
            GET_ALL_URL,
            data=self.create_sale,
            content_type='application/json')

    def test_add_sale(self):
        """ Test for sale order creation """

        resource = self.client.post(
            GET_ALL_URL,
            data=self.create_sale,
            content_type='application/json')

        data = json.loads(resource.data.decode())
        print(data)
        self.assertEqual(resource.status_code, 201)
        self.assertEqual(resource.content_type, 'application/json')

    def test_get_all_sales(self):
        """ Test for getting all sales record """
        resource = self.client.get(
            GET_ALL_URL,
            data=json.dumps(dict()),
            content_type='application/json')

        data = json.loads(resource.data.decode())
        print(data)
        self.assertEqual(resource.status_code, 200)
        self.assertEqual(resource.content_type, 'application/json')
