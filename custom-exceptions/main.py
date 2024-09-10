class OutOfStockError(Exception):
    """Exception raised when the product is out of stock"""

    def __init__(self, product_name):
        self.product_name = product_name
        super().__init__(f"'{self.product_name}' is out of stock")


class InvalidProductIDError(Exception):
    """Exception raised for invalid product IDs"""

    def __init__(self, product_id):
        self.product_id = product_id
        super().__init__(f"Product ID '{self.product_id}' is not valid")


class PurchaseLimitExceededError(Exception):
    """Exception raised when purchase limit is exceeded"""

    def __init__(self, product_name, limit):
        self.product_name = product_name
        self.limit = limit
        super().__init__(
        	f"Cannot purchase more than {self.limit} units of '{self.product_name}'"
    	)

class Inventory:
    def __init__(self):
        self.products = {
        	'P001': {'name': 'Laptop', 'stock': 5, 'max_purchase_limit': 2},
        	'P002': {'name': 'Smartphone', 'stock': 0, 'max_purchase_limit': 5},
    	}


    def purchase(self, product_id, quantity):
        if product_id not in self.products:
            raise InvalidProductIDError(product_id)
    
        product = self.products[product_id]

        if product['stock'] == 0:
            raise OutOfStockError(product['name'])

        # Check if the quantity exceeds the max purchase limit
        if quantity > product['max_purchase_limit']:
            raise PurchaseLimitExceededError(product['name'], product['max_purchase_limit'])

        # Process purchase
        if quantity <= product['stock']:
            product['stock'] -= quantity
            print(f"Successfully purchased {quantity} unit(s) of {product['name']}.")
        else:
            raise OutOfStockError(product['name'])

# Testing the system
inventory = Inventory()

try:
    inventory.purchase('P001', 1)  # Successful purchase
    inventory.purchase('P002', 1)  # OutOfStockError
except OutOfStockError as e:
    print(f"Error: {e}")
except InvalidProductIDError as e:
    print(f"Error: {e}")
except PurchaseLimitExceededError as e:
    print(f"Error: {e}")

try:
    inventory.purchase('P001', 3)  # PurchaseLimitExceededError
except OutOfStockError as e:
    print(f"Error: {e}")
except InvalidProductIDError as e:
    print(f"Error: {e}")
except PurchaseLimitExceededError as e:
    print(f"Error: {e}")

