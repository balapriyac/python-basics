# Bad example
def process(d, t):
    return d * (1 + t/100)

# Good example
def apply_tax_to_price(price, tax_rate):
    return price * (1 + tax_rate/100)

# Bad example
def send_notification(user_id, email, phone, message, subject, 
                     priority, send_email, send_sms, attachment):
    # code goes here...

# Good example
def send_notification(user, notification_config, message_content):
    """
    Send a notification to a user based on configuration settings.
    
    Parameters:
    - user: User object with contact information
    - notification_config: NotificationConfig with delivery preferences
    - message_content: MessageContent with subject, body, and attachments
    """
    # code goes here...

# Bad example
def process_order(order):
    # Validate order
    # Update inventory
    # Charge customer
    # Send confirmation email
    # Update analytics

# Good example
def process_order(order):
    """Process a customer order from validation through confirmation."""
    validated_order = validate_order(order)
    update_inventory(validated_order)
    payment_result = charge_customer(validated_order)
    if payment_result.is_successful:
        send_confirmation_email(validated_order, payment_result)
        update_order_analytics(validated_order)
    return OrderResult(validated_order, payment_result)

# Bad example
def calculate_final_price(price, discount):
    return price * (1 - discount / 100)

# Good example
def calculate_final_price(price: float, discount_percentage: float) -> float:
    """
    Calculate final price after applying the discount.
    
    Parameters:
    - price: Original price of the item
    - discount_percentage: Percentage discount to apply (0-100)
    
    Returns:
    - Discounted price
    """
    return price * (1 - discount_percentage / 100)
# Bad example
def validate_email(email):
    """This function validates email."""
    # code goes here...

# Good example
def validate_email(email: str) -> bool:
    """
    Check if an email address has valid format.
    
    Parameters:
    - email: String containing the email address to validate
    
    Returns:
    - True if the email is valid, else False
    
    Note:
    - This validation checks format only, not if the address actually exists
    """
    # code goes here...
