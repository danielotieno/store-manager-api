""" Creating data Table scripts """

users = """ CREATE TABLE IF NOT EXISTS users_table(
    userid serial PRIMARY KEY,
    username VARCHAR(250) NOT NULL,
    email VARCHAR(250) UNIQUE,
    password VARCHAR(250) NOT NULL,
    user_role VARCHAR(250) NOT NULL DEFAULT 'Store_Attendant',
    created_at timestamp with time zone DEFAULT now()
    );
"""

categories = """ CREATE TABLE IF NOT EXISTS categories_table(
    category_id serial PRIMARY KEY,
    category_name VARCHAR(50) NOT NULL,
    category_status VARCHAR(50) NOT NULL,
    created_at timestamp with time zone DEFAULT now()
    );
"""


products = """ CREATE TABLE IF NOT EXISTS products_table(
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

sales = """ CREATE TABLE IF NOT EXISTS sales_table(
    sale_id serial PRIMARY KEY,
    customer VARCHAR(50) NOT NULL,
    product VARCHAR(50) NOT NULL,
    quantity INTEGER NOT NULL,
    created_by VARCHAR(50) NOT NULL,
    total_amount INTEGER NOT NULL,
    created_at timestamp with time zone DEFAULT now()
    );
"""


blacklisted_tokens = """ CREATE TABLE IF NOT EXISTS blacklisted_table(
    black_id serial PRIMARY KEY,
    token VARCHAR(255) NOT NULL,
    created_at timestamp with time zone DEFAULT now()
    );
"""

drop_users = """ DROP TABLE IF EXISTS users_table CASCADE """
drop_categories = """ DROP TABLE IF EXISTS categories_table CASCADE """
drop_products = """ DROP TABLE IF EXISTS products_table CASCADE """
drop_sales = """ DROP TABLE IF EXISTS sales_table CASCADE """
drop_blacklisted_tokens = """ DROP TABLE IF EXISTS blacklisted_table CASCADE """

tables_to_drop = [drop_users, drop_categories, drop_products,
                  drop_sales, drop_blacklisted_tokens]

table_list = [users, categories, products, sales, blacklisted_tokens]
