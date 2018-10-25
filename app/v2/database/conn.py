""" Database initialize file """
import os
import psycopg2

from flask import current_app


# Local imports

from app.v2.database.tables import table_list, tables_to_drop


def database_connection():
    """ create a database connection  """

    url = os.getenv('DATABASE_URL')
    return psycopg2.connect(url)


def init_database():
    """Initialize a database"""
    try:
        connection = database_connection()
        connection.autocommit = True

        # activate cursor
        cursor = connection.cursor()

        for table in table_list:
            cursor.execute(table)
        connection.commit()

        create_admin()

    except (Exception, psycopg2.DatabaseError) as error:
        print("DB Error")
        print(error)


def create_admin():
    """create a default admin user"""
    conn = database_connection()
    cur = conn.cursor()

    # check if user exists
    email = "admin@email.com"
    password = "admin12345"
    cur.execute("SELECT * FROM users_table WHERE email=%(email)s",
                {'email': email})
    if cur.rowcount > 0:
        return False
    cur.execute("INSERT INTO users_table(username, email, password, user_role)\
    VALUES(%(username)s, %(email)s, %(password)s, %(user_role)s);",
                {'username': 'admin', 'email': 'admin@email.com', 'password': password, 'user_role': 'Admin'})
    conn.commit()


def drop_all_tables():
    """A method to drop tables """
    connection = database_connection()
    cursor = connection.cursor()
    for drop in tables_to_drop:
        cursor.execute(drop)
        connection.commit()
    connection.close()
