""" Database initialize file """
import os
import psycopg2


# Local imports

from app.v2.database.tables import table_list, tables_to_drop


def database_connection():
    """ create a database connection  """

    url = os.getenv('DATABASE_URL')
    return psycopg2.connect(url)


def init_db():
    """Initialize a database"""
    try:
        connection = dbcon()
        connection.autocommit = True

        # activate cursor
        cursor = connection.cursor()

        for table in table_list:
            cursor.execute(query)
        connection.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print("DB Error")
        print(error)


def drop_all_tables():
    """A method to drop tables """
    connection = database_connection()
    cursor = connection.cursor()
    for drop in tables_to_drop:
        cursor.execute(drop)
        connection.commit()
    connection.close()
