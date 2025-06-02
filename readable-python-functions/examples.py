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
