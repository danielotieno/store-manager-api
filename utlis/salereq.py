def validate_data(data):
    """validate product details"""
    try:
        # check if customer name is empty
        if data["customer"] is False:
            return "Customer name is required"
            # check if product name is empty
        elif data["product"] is False:
            return "Product name is required"
            # check if quantity field is empty
        elif data["quantity"] is False:
            return "quantity is required"
            # check if total amount field is empty
        elif data["total_amount"] is False:
            return "total amount is required"
        else:
            return "valid"
    except Exception as error:
        return "please provide all the fields, missing " + str(error)
