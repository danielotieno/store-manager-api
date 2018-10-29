""" Database initialize file """
import os
import psycopg2

# Local imports
from app.v2.database.tables import TABLE_LIST, TABLES_TO_DROP


def database_connection(config=None):
    """ create a database connection """
    if config == 'testing':
        database_url = os.getenv(
            'DATABASE_TEST_URL', 'postgres://vgzssioscyqndx:656c03a65f21725b34cfa614b1cb2d8f4bed33deda3e938426ee47ced665f1ee@ec2-54-204-46-60.compute-1.amazonaws.com:5432/dckpotr4cr2na0')
    else:
        database_url = os.getenv(
            'DATABASE_URL', 'postgres://vgzssioscyqndx:656c03a65f21725b34cfa614b1cb2d8f4bed33deda3e938426ee47ced665f1ee@ec2-54-204-46-60.compute-1.amazonaws.com:5432/dckpotr4cr2na0')

    # Connect to an existing database
    return psycopg2.connect(database_url)


def init_database():
    """Initialize a database"""
    try:
        connection = database_connection()
        connection.autocommit = True

        # activate cursor
        cursor = connection.cursor()

        for table in TABLE_LIST:
            # Execute a command: this creates a new table
            cursor.execute(table)

        # Make the changes to the database persistent
        connection.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print("DB Error")
        print(error)


def create_admin():
    """create a default admin user"""
    conn = database_connection()
    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Add default user admin details
    username = os.getenv('ADMIN_USERNAME')
    email = os.getenv('ADMIN_EMAIL')
    password = os.getenv('ADMIN_PASS')
    role = os.getenv('ROLE')

    # Check if user exists
    cur.execute("SELECT * FROM users_table WHERE email=%(email)s",
                {'email': email})
    if cur.rowcount > 0:
        return False
    cur.execute("INSERT INTO users_table(username, email, password, user_role)\
    VALUES(%(username)s, %(email)s, %(password)s, %(user_role)s);", {'username': username, 'email': email, 'password': password, 'user_role': role})
    conn.commit()


def drop_all_tables():
    """A method to drop tables """
    connection = database_connection()
    cursor = connection.cursor()
    for drop in TABLES_TO_DROP:
        cursor.execute(drop)
        connection.commit()
    connection.close()
