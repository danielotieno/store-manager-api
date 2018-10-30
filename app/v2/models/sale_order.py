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

    def create_sale(self, customer, product_name, quantity, created_by, total_amount):
        """Create sale item in table and update product quantity"""

        # Get quantity from products table
        self.cur.execute("SELECT quantity FROM products_table WHERE product_name=%(product_name)s", {
            'product_name': product_name})

        # Get the product if name exists
        product_quantity = self.cur.fetchone()

        if product_quantity:
            self.cur.execute(
                "INSERT INTO sales_table(customer, product_name, quantity, created_by, total_amount)\
            VALUES(%(customer)s, %(product_name)s, %(quantity)s, %(created_by)s, %(total_amount)s);", {'customer': customer, 'product_name': product_name, 'quantity': quantity, 'created_by': created_by, 'total_amount': total_amount})
            self.conn.commit()

            # Calculate remaining quantity
            quantity_balance = product_quantity[0] - quantity

            # Update quantity in products table with remaning quantity
            self.cur.execute(
                "UPDATE products_table SET quantity=%s WHERE product_name=%s", (quantity_balance, product_name))
            self.conn.commit()
            return {"message": "Sale Order successfully created"}, 201
        return {"message": "Product Not Found"}, 404

    def get_sales(self):
        """ A method to get all sales record """
        self.cur.execute("SELECT * FROM sales_table")
        if self.cur.rowcount > 0:
            rows = self.cur.fetchall()
            self.sales_list = []
            for sale in rows:
                self.sales_details.update({
                    'sale_id': sale[0],
                    'customer': sale[1],
                    'product_name': sale[2],
                    'quantity': sale[3],
                    'created_by': sale[4],
                    'total_amount': sale[5]})
                self.sales_list.append(dict(self.sales_details))
            return {
                "message": "Successfully",
                "Products": self.sales_details}, 200
        return {
            "message": "Sales Record Not Found"}, 200

    def get_sale_record_by_id(self, sale_id):
        """ A method to get a single sale record """
        self.cur.execute(
            "SELECT * FROM sales_table WHERE sale_id=%(sale_id)s", {'sale_id': sale_id})
        if self.cur.rowcount > 0:
            rows = self.cur.fetchone()
            self.sales_details.update({
                'sale_id': rows[0],
                'customer': rows[1],
                'product_name': rows[2],
                'quantity': rows[3],
                'created_by': rows[4],
                'total_amount': rows[5]})
            return {
                "message": "Successful",
                "Product": self.sales_details}, 200
        return {"message": "Sale Record Not Found."}, 400
