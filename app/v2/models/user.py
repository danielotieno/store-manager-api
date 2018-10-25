"""
This model defines a user class and it's methods
It also create data structure to store user data

"""
from datetime import datetime
from werkzeug.security import check_password_hash, generate_password_hash

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
            sql = 'UPDATE {} SET {} WHERE id={}'.format(table, string, id)
            cur.execute(sql)
            conn.commit()

    @staticmethod
    def delete(table, id):
        """ A method to delete a table """
        sql = 'DELETE FROM {} WHERE id={}'.format(table, id)
        cur.execute(sql)
        conn.commit()


class User(Start):
    """ A class to handle activities related to a user """

    def __init__(self, username, email, password, role='Store_Attendant'):
        """ A constructor method for creating a user """
        self.id = None
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        self.role = role
        self.created_at = datetime.utcnow().isoformat()

    def add_user(self):
        '''Method for adding input into users table'''
        cur.execute(
            """
            INSERT INTO users_table(username, email, password, role)
            VALUES(%s,%s,%s,%s)""",
            (self.username, self.email, self.password, self.role))
        self.save()

    @staticmethod
    def to_json(user):
        """ Convert user list to json """
        return dict(
            id=user[0],
            username=user[1],
            email=user[2],
            role=user[4]
        )

    def validate_password(self, password):
        """ Method for validating password input """
        if check_password_hash(self.password, password):
            return True
        return False

    @classmethod
    def get_user_by_username(cls, username):
        """ Method for getting user by username """
        cur.execute(
            "SELECT * FROM users_table WHERE username=%s", (username,))
        user = cur.fetchone()

        if user:
            return user.to_json()
        return None

    @classmethod
    def get_user_by_id(cls, id):
        """ Get user given a user id"""
        cur.execute(
            "SELECT * FROM users_table WHERE userid=%s", (userid,))
        user = cur.fetchone()

        if user:
            return user.to_json()
        return None

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
