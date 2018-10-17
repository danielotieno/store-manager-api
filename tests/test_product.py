import unittest
import json


from app.v1 import create_app


ADD_ENTRY_URL = '/api/v1/products/7'
ADD_UPDATE_URL = '/api/v1/products/8'
GET_SINGLE_URL = '/api/v1/products/1'
GET_ALL_URL = '/api/v1/products'
DELETE_URL = '/api/v1/products/2'
MODIFY_URL = '/api/v1/products/8'


class TestBase(unittest.TestCase):
    """ Class for setup tests """

    def create_app(self):
        """ Add Test configuration """
        config_name = 'testing'
        app = create_app(config_name)

        self.create_product = json.dumps(dict(
            name="Shirt",
            description="Modern polo shirt",
            price=350,
            category="Polo",
            low_inventory=10))
        self.client = app.test_client()
        self.client.post(
            GET_ALL_URL,
            data=self.create_product,
            content_type='application/json')

        return app


class TestProducts(TestBase):

    def test_add_a_product(self):
        """ Test to add a product """
        resource = self.client.post(
            GET_ALL_URL,
            data=self.create_product,
            content_type='application/json')

        data = json.loads(resource.data.decode('utf-8'))
        print(data)
        self.assertEqual(resource.status_code, 201)
        self.assertEqual(resource.content_type, 'application/json')

    def test_get_all_products(self):
        """ Test to get all products """

        response = self.client.get(
            GET_ALL_URL, content_type='application/json')

        data = json.loads(response.data.decode('utf-8'))
        print(data)
        self.assertEqual(response.content_type, 'application/json')
        self.assertEqual(response.status_code, 200)

    def test_get_specific_product(self):
        """ Test to fetch a specific product by id """

        response = self.client.get(
            GET_SINGLE_URL, data=json.dumps(dict(name="Shirt",
                                                 description="Modern polo shirt",
                                                 price=350,
                                                 category="Polo",
                                                 low_inventory=10
                                                 )), content_type='application/json')
        result = json.loads(response.data.decode('utf-8'))
        print(result)
        self.assertEqual(response.status_code, 200)

    def test_update_a_product(self):
        """ Test to update a product """
        response = self.client.post(GET_ALL_URL, data=self.create_product,
                                    content_type='application/json')

        data = json.loads(response.data.decode('utf-8'))
        print(data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.content_type, 'application/json')

        response = self.client.put(MODIFY_URL,
                                   data=json.dumps(dict(
                                       name="Shirt",
                                       description="Modern polo shirt",
                                       price=500,
                                       category="Gucci",
                                       low_inventory=10


                                   )), content_type=("application/json"))
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data.decode())
        print(result)

    def test_delete_an_order(self):
        """ Test to delete a product """
        response = self.client.delete(
            DELETE_URL, data=json.dumps(dict(product_id=2,
                                             name="Jeans",
                                             description="Brand new khaki jeans",
                                             price=500,
                                             category="Khaki",
                                             low_inventory=10
                                             )), content_type='application/json')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
