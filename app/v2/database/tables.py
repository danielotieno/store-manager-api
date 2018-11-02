""" Creating data Table scripts """

USERS = """ CREATE TABLE IF NOT EXISTS users_table(
    userid serial PRIMARY KEY,
    username VARCHAR(250) NOT NULL,
    email VARCHAR(250) UNIQUE,
    password VARCHAR(250) NOT NULL,
    user_role VARCHAR(250) NOT NULL DEFAULT 'Store_Attendant'
    );
"""

CATEGORIES = """ CREATE TABLE IF NOT EXISTS categories_table(
    category_id serial PRIMARY KEY,
    category_name VARCHAR(50) UNIQUE,
    category_status VARCHAR(50) NOT NULL
    );
"""


PRODUCTS = """ CREATE TABLE IF NOT EXISTS products_table(
    product_id serial PRIMARY KEY,
    product_name VARCHAR(50) NOT NULL,
    product_description VARCHAR(50) NOT NULL,
    category VARCHAR(50) NOT NULL,
    price INTEGER NOT NUll,
    quantity INTEGER NOT NULL,
    low_inventory INTEGER NOT NULL
    );
"""

SALES = """ CREATE TABLE IF NOT EXISTS sales_table(
    sale_id serial PRIMARY KEY,
    created_by VARCHAR(250) NOT NULL,
    total_amount INTEGER NOT NULL
    );
"""

CART = """ CREATE TABLE IF NOT EXISTS cart_table(
    sale_id INT REFERENCES sales_table(sale_id) ON UPDATE CASCADE ON DELETE CASCADE,
    product_id INTEGER REFERENCES products_table (product_id) ON UPDATE CASCADE,
    price INTEGER NOT NUll,
    quantity INTEGER NOT NULL
    );
"""


BLACKLISTED_TOKENS = """ CREATE TABLE IF NOT EXISTS blacklisted_table(
    black_id serial PRIMARY KEY,
    token VARCHAR(255) NOT NULL
    );
"""

EXT = """ CREATE EXTENSION IF NOT EXISTS citext; """
ALT_PRODUCT = """ ALTER TABLE products_table ALTER COLUMN product_name TYPE citext; """
ALT_CATEGORY = """ ALTER TABLE categories_table ALTER COLUMN category_name TYPE citext; """
ALT_STATUS = """ ALTER TABLE categories_table ALTER COLUMN category_status TYPE citext; """

DROP_USERS = """ DROP TABLE IF EXISTS users_table CASCADE """
DROP_CATEGORIES = """ DROP TABLE IF EXISTS categories_table CASCADE """
DROP_PRODUCTS = """ DROP TABLE IF EXISTS products_table CASCADE """
DROP_SALES = """ DROP TABLE IF EXISTS sales_table CASCADE """
DROP_CART = """ DROP TABLE IF EXISTS cart_table CASCADE """
DROP_BLACKLISTED_TOKENS = """ DROP TABLE IF EXISTS blacklisted_table CASCADE """

TABLES_TO_DROP = [DROP_USERS, DROP_CATEGORIES, DROP_PRODUCTS,
                  DROP_SALES, DROP_BLACKLISTED_TOKENS]

TABLE_LIST = [USERS, CATEGORIES, PRODUCTS,
              SALES, CART, BLACKLISTED_TOKENS, EXT, ALT_PRODUCT, ALT_CATEGORY, ALT_STATUS]
