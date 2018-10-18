"""
This model defines a user class and it's methods
It also create data structure to store user data

"""
from datetime import datetime, timedelta
from flask import current_app
from werkzeug.security import check_password_hash, generate_password_hash


class Model():
    """Class for user data structure"""

    def __init__(self):
        self.users = {}
        self.user_count = 0

    def drop(self):
        self.__init__()


DB = Model()


class Start():
    """Start class to be inherited by User classes"""

    def update(self, data):
        # Validate keys before passing to data.
        for key in data:
            setattr(self, key, data[key])
        setattr(self, 'last_modified', datetime.utcnow().isoformat())
        return self.view()


class User(Start):
    """ A class to handle activities related to a user """

    def __init__(self, username, email, password, role):
        """ A constructor method for creating a user """
        self.id = None
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        self.role = role
        self.created_at = datetime.utcnow().isoformat()

    def validate_password(self, password):
        """ Method for validating password input """
        if check_password_hash(self.password, password):
            return True
        return False

    def save(self):
        """ Method for saving user registration details """
        setattr(self, 'id', DB.user_count + 1)
        DB.users.update({self.id: self})
        DB.user_count += 1
        return self.view()

    @classmethod
    def get_user_by_username(cls, username):
        """ Method for getting user by username """
        for id_ in DB.users:
            user = DB.users.get(id_)
            if user.username == username:
                return user
        return None

    @classmethod
    def get_user_by_id(cls, id):
        """ Get user given a user id"""
        user = DB.users.get(id)
        if not user:
            return {'message': 'User does not exist.'}
        return user

    @classmethod
    def get_user_by_email(cls, email):
        """ Method for getting user by email"""
        for id_ in DB.users:
            user = DB.users.get(id_)
            if user.email == email:
                return user
        return None

    def view(self):
        """ Method to jsonify object user"""
        keys = ['username', 'email', 'id', 'role']
        return {key: getattr(self, key) for key in keys}

    def delete_user(self):
        """ Method for deleting a user"""
        del DB.users[self.id]
