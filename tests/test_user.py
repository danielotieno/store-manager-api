"""This module defines tests for the user class and its methods"""
import json

from .start import BaseClass

SIGNUP_URL = '/api/v1/user/signup'
LOGIN_URL = '/api/v1/user/login'


class UserTests(BaseClass):
    """ Defining and setup user class tests """

    def test_user_registration(self):
        """ Test user registration works correcty """
        response = self.client.post(SIGNUP_URL,
                                    data=json.dumps(self.user_data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        result = json.loads(response.data.decode())
        self.assertEqual(result["message"],
                         "registration successful, now login")
