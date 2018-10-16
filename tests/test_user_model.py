from app.v1.models.user import User, DB
from .start import BaseClass


class TestUserModel(BaseClass):
    """ Class to test user model """

    def test_get_user(self):
        """ Test can get user """
        self.user1.save()
        user = User.get_user_by_id(id=1)
        self.assertIsInstance(user, User)
        keys = sorted(list(user.view().keys()))
        self.assertListEqual(keys, sorted(['username', 'email', 'id', 'role']))

    def test_get_non_existent_user(self):
        """ Test cannot get non existent user """
        user = User.get_user_by_id(id=4)
        self.assertEqual('User does not exist.', user['message'])

    def test_can_save_user(self):
        """Test successful save operation for user"""
        user = self.user1.save()
        self.assertEqual(1, len(DB.users))
        self.assertTrue(isinstance(user, dict))

    def test_can_update_user_details(self):
        """Test successful update of user deatails"""
        data = {
            'username': 'newusername',
            'email': 'newusername@email.com',
            'role': 'Store Attendant'}
        self.user1.save()
        user = User.get_user_by_id(id=1)
        user = user.update(data=data)
        self.assertEqual(data['username'], user['username'])
        self.assertEqual(data['email'], user['email'])
        self.assertEqual(data['role'], user['role'])

    def test_can_delete_user(self):
        """Test suucessful deletion of user"""
        self.user1.save()
        self.assertEqual(1, len(DB.users))
        user = User.get_user_by_id(id=1)
        user.delete_user()
        self.assertEqual(0, len(DB.users))
