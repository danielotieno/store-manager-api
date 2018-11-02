"""
This model defines a sales order class and it's methods
It also create data structure to store sales order data

"""
from app.v2.database.conn import database_connection
from flask_jwt_extended import get_jwt_identity
from .product import Product

product_obj = Product()


class Sale:
    """ Create a Sale class to hold sales methods """

    def __init__(self):
        """ Initialize sales database table """
        self.conn = database_connection()
        self.conn.autocommit = True
        self.cur = self.conn.cursor()
        self.sales_list = []
        self.sales_details = {}

    def create_sale(self, cart):
        """Add sale item in table """
        total = 0
        for item in cart:
            res = product_obj.get_product_by_id(item['product_id'])
            if res[0]['message'] == "Product Not Found.":
                msg = str(item['product_id'])
                return {"message": "product with " + msg + " doesnt exist"}
            else:
                product_price = res[0]['Product']['price']
                total = product_price + total

        created_by = get_jwt_identity()
        self.cur.execute(
            """INSERT INTO sales_table(created_by, total_amount)
            VALUES(%s,%s)""", (created_by[2], total)
        )
        self.cur.execute("SELECT * from sales_table")
        self.conn.commit()
        sales = self.cur.fetchall()
        last_index = len(sales) - 1
        sale_id = sales[last_index][0]

        for item in cart:
            product_id = item["product_id"]
            quantity = item["quantity"]
            get_data = product_obj.get_product_by_id(product_id)
            price = get_data[0]['Product']['price']
            current_qty = get_data[0]['Product']['quantity']

            self.cur.execute(
                """INSERT INTO cart_table(sale_id, product_id, price, quantity)
                VALUES(%s, %s, %s, %s)""", (sale_id, product_id, price, quantity)
            )
            self.conn.commit()
            balance_qty = current_qty - quantity
            self.update_quantity(product_id, balance_qty)
        return self.get_sale_record_by_id(sale_id)

    def update_quantity(self, product_id, quantity):
        """Update product quantity"""
        self.cur.execute(
            """UPDATE products_table SET quantity = %s where product_id = %s""", (
                quantity, product_id)
        )
        self.conn.commit()

    def get_sales(self):
        """A method to get all sales record"""
        self.cur.execute("SELECT * from sales_table")
        rows = self.cur.fetchall()
        sale_list = []
        for row in rows:
            sale = {}
            sale["sale_id"] = row[0]
            sale["customer"] = row[1]
            sale["created_by"] = row[2]
            sale["total_amount"] = row[3]
            sale_list.append(sale)
        for sale in sale_list:
            sale["products"] = []
            self.cur.execute(
                "SELECT * from cart_table where sale_id = %s" % sale["sale_id"])
            items = self.cur.fetchall()
            for item in items:
                product = {}
                product["product_name"] = item[1]
                product["price"] = item[2]
                product["quantity"] = item[3]
                sale["products"].append(product)
        return sale_list

    def get_sale_record_by_id(self, sale_id):
        """ A method to get a single sale record """
        self.cur.execute(
            "SELECT * FROM sales_table WHERE sale_id=%(sale_id)s", {'sale_id': sale_id})
        if self.cur.rowcount > 0:
            rows = self.cur.fetchall()
            print("sales here")
            print(rows)
            if not rows:
                return rows
            sale = {}
            for row in rows:
                sale["sale_id"] = row[0]
                sale["created_by"] = row[1]
                sale["total_amount"] = row[2]
            sale["products"] = []
            self.cur.execute(
                "SELECT * from cart_table where sale_id = %s" % sale["sale_id"])
            items = self.cur.fetchall()
            for item in items:
                product = {}
                product["product_name"] = item[1]
                product["price"] = item[2]
                product["quantity"] = item[3]
                sale["products"].append(product)
            return sale
        return {"message": "Sale Record Not Found."}, 400
