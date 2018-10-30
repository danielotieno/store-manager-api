""" Creating data Table scripts """

USERS = """ CREATE TABLE IF NOT EXISTS users_table(
    userid serial PRIMARY KEY,
    username VARCHAR(250) NOT NULL,
    email VARCHAR(250) UNIQUE,
    password VARCHAR(250) NOT NULL,
    user_role VARCHAR(250) NOT NULL DEFAULT 'Store_Attendant',
    created_at timestamp with time zone DEFAULT now()
    );
"""

CATEGORIES = """ CREATE TABLE IF NOT EXISTS categories_table(
    category_id serial PRIMARY KEY,
    category_name VARCHAR(50) NOT NULL,
    category_status VARCHAR(50) NOT NULL,
    created_at timestamp with time zone DEFAULT now()
    );
"""


PRODUCTS = """ CREATE TABLE IF NOT EXISTS products_table(
    product_id serial PRIMARY KEY,
    product_name VARCHAR(50) NOT NULL,
    product_description VARCHAR(50) NOT NULL,
    price INTEGER NOT NUll,
    category VARCHAR(50) NOT NULL,
    quantity INTEGER NOT NULL,
    low_inventory INTEGER NOT NULL,
    created_at timestamp with time zone DEFAULT now()
    );
"""

SALES = """ CREATE TABLE IF NOT EXISTS sales_table(
    sale_id serial PRIMARY KEY,
    customer VARCHAR(50) NOT NULL,
    product_name VARCHAR(50) NOT NULL,
    quantity INTEGER NOT NULL,
    created_by VARCHAR(50) NOT NULL,
    total_amount INTEGER NOT NULL,
    created_at timestamp with time zone DEFAULT now()
    );
"""


BLACKLISTED_TOKENS = """ CREATE TABLE IF NOT EXISTS blacklisted_table(
    black_id serial PRIMARY KEY,
    token VARCHAR(255) NOT NULL,
    created_at timestamp with time zone DEFAULT now()
    );
"""

DROP_USERS = """ DROP TABLE IF EXISTS users_table CASCADE """
DROP_CATEGORIES = """ DROP TABLE IF EXISTS categories_table CASCADE """
DROP_PRODUCTS = """ DROP TABLE IF EXISTS products_table CASCADE """
DROP_SALES = """ DROP TABLE IF EXISTS sales_table CASCADE """
DROP_BLACKLISTED_TOKENS = """ DROP TABLE IF EXISTS blacklisted_table CASCADE """

TABLES_TO_DROP = [DROP_USERS, DROP_CATEGORIES, DROP_PRODUCTS,
                  DROP_SALES, DROP_BLACKLISTED_TOKENS]

TABLE_LIST = [USERS, CATEGORIES, PRODUCTS, SALES, BLACKLISTED_TOKENS]
