from app.v1.models.user import User, DB
from .start import BaseClass


class TestUserModel(BaseClass):
    """ Class to test user model """

    def test_get_user(self):
        '''Test can get user'''
        self.user1.save()
        user = User.get_user_by_id(id=1)
        self.assertIsInstance(user, User)
        keys = sorted(list(user.view().keys()))
        self.assertListEqual(keys, sorted(['username', 'email', 'id', 'role']))
