""" Tests for user model """
from app.v2.models.user import User
from .start import BaseClass


class TestUserModel(BaseClass):
    """ Class to test user model """

    def test_can_create_user(self):
        '''Test successful account creation for user'''
        self.user1.add_user()
        u = self.user_model.get('users_table', username=self.user1.username)
        self.assertEqual(u[1], self.user1.username)

    def test_can_delete_user(self):
        '''Test successful deletion of user'''
        self.user1.add_user()
        user = self.user_model.get('users_table')
        self.user_model.delete('users_table', 1)
        user = self.user_model.get('users_table')
        self.assertIsNone(user)

    def test_get_non_existent_user(self):
        '''Test model cannot get a non-existent user'''
        user = self.user_model.get('users_table', userid=3)
        self.assertIsNone(user)

    def test_get_user(self):
        '''Test can successfully get a user'''
        self.user1.add_user()
        user = self.user_model.get('users_table', username="testuser")
        user = self.user_model.to_json(user)
        self.assertEqual(user['username'], "testuser")

    def test_can_update_user_details(self):
        '''Test successful update of user'''
        self.user1.add_user()
        initial_user_details = self.user_model.get(
            'users_table', username="testuser")
        self.user_model.update('users_table', 2, {'username': 'NewTestUser'})
        updated_user_details = self.user_model.get(
            'users_table', username="NewTestUser")
        self.assertNotEqual(initial_user_details, updated_user_details)
