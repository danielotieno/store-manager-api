"""
This model defines a sales order class and it's methods
It also create data structure to store sales order data

"""
from app.v2.database.conn import database_connection


class Sale:
    """ Create a Sale class to hold sales methods """

    def __init__(self):
        """ Initialize sales database table """
        self.conn = database_connection()
        self.conn.autocommit = True
        self.cur = self.conn.cursor()
        self.sales_list = []
        self.sales_details = {}

    def create_sale(self, products, total_amount):
        """Add sale item in table """
        self.cur.execute(
            """INSERT INTO sales_table(total_amount)
            VALUES(%s, %s, %s)""", (total_amount)
        )

        sale_id = self.cur.fetchone()[0]
        self.conn.commit()

        for item in products:
            product_name = item["product_name"]
            quantity = item["quantity"]
            price = item["price"]
            self.cur.execute(
                """INSERT INTO cart_table(sale_id, product_name, price, quantity)
                VALUES(%s, %s, %s, %s)""", (sale_id, product_name, price, quantity)
            )
            self.conn.commit()

    def update_quantity(self, product_name, quantity):
        """Update product quantity"""
        self.cur.execute(
            """UPDATE products_table SET quantity = %s where product_name = %s""", (
                quantity, product_name)
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
            if not rows:
                return rows
            sale = {}
            for row in rows:
                sale["sale_id"] = row[0]
                sale["created_by"] = row[1]
                sale["total_amount"] = row[3]
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
