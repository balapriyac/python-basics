class OrderError(Exception):
    """Base exception for order-related errors"""
    pass

class PaymentError(OrderError):
    """Raised when payment processing fails"""
    def __init__(self, message, transaction_id=None):
        self.transaction_id = transaction_id
        super().__init__(f"Payment failed: {message}")

class InventoryError(OrderError):
    """Raised when inventory is insufficient"""
    def __init__(self, product_id, requested, available):
        self.product_id = product_id
        self.requested = requested
        self.available = available
        super().__init__(
            f"Insufficient inventory for product {product_id}: "
            f"requested {requested}, available {available}"
        )

# Usage example
def process_order(order):
    try:
        check_inventory(order)
        process_payment(order)
    except InventoryError as e:
        # Handle inventory issues
        notify_inventory_team(e.product_id)
        raise
    except PaymentError as e:
        # Handle payment issues
        if e.transaction_id:
            reverse_transaction(e.transaction_id)
        raise
      
