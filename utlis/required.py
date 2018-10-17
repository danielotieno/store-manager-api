def required(var):
    """checks if any required field is blank"""
    if var.strip() == '':
        return 'All fields are required'
    return None


def validate_data(data):
    """validate product details"""
    try:
        # check if name is empty
        if data["name"] is False:
            return "Product name is required"
            # check description is empty
        elif data["description"] is False:
            return "Product description is required"
            # check if price field is empty
        elif data["price"] is False:
            return "price is required"
            # check if category field is empty
        elif data["category"] is False:
            return "category is required"
            # check if quantity field is empty
        elif data["quantity"] is False:
            return "quantity is required"
            # check if price field is empty
        elif data["low_inventory"] is False:
            return "This field is required"
        else:
            return "valid"
    except Exception as error:
        return "please provide all the fields, missing " + str(error)
