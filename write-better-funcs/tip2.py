# fn. to process orders
def process_orders(orders):
    total_quantity = sum(order['quantity'] for order in orders)
    total_value = sum(order['quantity'] * order['price'] for order in orders)
    return {
        'total_quantity': total_quantity,
        'total_value': total_value
    }

# Sample data
orders = [
    {'price': 100.0, 'quantity': 2},
    {'price': 50.0, 'quantity': 5},
    {'price': 150.0, 'quantity': 1}
]

# Usage
result = process_orders(orders)
print(result) 

# modified with type hints
from typing import List, Dict

def process_orders(orders: List[Dict[str, float | int]]) -> Dict[str, float | int]:
    total_quantity = sum(order['quantity'] for order in orders)
    total_value = sum(order['quantity'] * order['price'] for order in orders)
    return {
        'total_quantity': total_quantity,
        'total_value': total_value
    }

# Sample data
orders = [
    {'price': 100.0, 'quantity': 2},
    {'price': 50.0, 'quantity': 5},
    {'price': 150.0, 'quantity': 1}
]

# Usage
result = process_orders(orders)
print(result)
