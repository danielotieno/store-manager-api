"""
This model defines a user class and it's methods
It also create data structure to store user data

"""
from datetime import datetime
from werkzeug.security import check_password_hash, generate_password_hash

from flask import current_app

from app.v2.database.conn import database_connection

conn = database_connection()
conn.autocommit = True
cur = conn.cursor()


class Start():
    """Start class to be inherited by User classes"""

    def save(self):
        """ Method for saving user registration details """
        conn.commit()

    @staticmethod
    def get(table_name, **kwargs):
        '''pass condition as keyword argument, just one'''
        for key, val in kwargs.items():
            sql = "SELECT * FROM {} WHERE {}='{}'".format(table_name, key, val)
            cur.execute(sql)
            item = cur.fetchone()
            return item

    @staticmethod
    def get_all(table_name):
        """ A method to get all tables """
        sql = 'SELECT * FROM {}'.format(table_name)
        cur.execute(sql)
        data = cur.fetchall()
        return data

    @staticmethod
    def update(table, id, data):
        """requires table as table name id as integer and data
        as a dictionary"""

        for key, val in data.items():
            string = "{}='{}'".format(key, val)
            sql = 'UPDATE {} SET {} WHERE userid={}'.format(table, string, id)
            cur.execute(sql)
            conn.commit()

    @staticmethod
    def delete(table, userid):
        """ A method to delete a table """
        sql = 'DELETE FROM {} WHERE userid={}'.format(table, userid)
        cur.execute(sql)
        conn.commit()


class User(Start):
    """ A class to handle activities related to a user """

    def __init__(self, username, email, password, user_role='Store_Attendant'):
        """ A constructor method for creating a user """
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        self.user_role = user_role
        self.created_at = datetime.utcnow().isoformat()

    def add_user(self):
        '''Method for adding input into users table'''
        cur.execute(
            """
            INSERT INTO users_table(username, email, password, user_role)
            VALUES(%s,%s,%s,%s)""",
            (self.username, self.email, self.password, self.user_role))
        self.save()

    @staticmethod
    def to_json(user):
        """ Convert user list to json """
        return dict(
            id=user[0],
            username=user[1],
            email=user[2],
            user_role=user[4]
        )

    @staticmethod
    def validate_password(password, email):
        """ Method for validating password input """
        user = User.get('users_table', email=email)
        if (user[3], password):
            return True
        return False

    @classmethod
    def get_user_by_username(cls, username):
        """ Method for getting user by username """
        cur.execute(
            "SELECT * FROM users_table WHERE username=%s", (username,))
        user = cur.fetchone()

        if user:
            return user
        return None

    @classmethod
    def get_user_by_id(cls, userid):
        """ Get user given a user id"""
        cur.execute(
            "SELECT * FROM users_table WHERE userid=%s", (userid,))
        user = cur.fetchone()

        if user:
            return user
        return None

    @classmethod
    def get_user_by_email(cls, email):
        """ Method for getting user by email"""
        cur.execute(
            "SELECT * FROM users_table WHERE email=%s", (email,))
        user = cur.fetchone()

        if user:
            return user
        return None

    @classmethod
    def delete_user(cls, id):
        """ Method for deleting a user"""
        cur.execute(
            "SELECT * FROM users_table WHERE userid=%(userid)s", {'userid': id})
        if cur.rowcount > 0:
            # delete this user details
            cur.execute(
                "DELETE FROM users_table WHERE userid=%(userid)s", {
                    'userid': id})
            conn.commit()
            return {"message": "Delete Successful."}, 201
        return {"message": "No user."}, 400
