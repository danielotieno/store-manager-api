"""This module defines tests for the user class and its methods"""
import unittest
from app.v1.models.user import User


class UserTests(unittest.TestCase):
    """Define and setup testing class"""

    def test_user_login(self):
        """Test if a user with valid details can login"""
        res = User().user_login("dan", "123456789")
        self.assertEqual(res, "Login successful")
