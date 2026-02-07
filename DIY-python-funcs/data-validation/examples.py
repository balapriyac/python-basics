import re

def validate_email(email):
    """
    Validate email addresses with practical rules.
    
    Returns (is_valid, error_message) tuple.
    """
    if not email or not isinstance(email, str):
        return False, "Email must be a non-empty string"
    
    email = email.strip()
    
    # Check length
    if len(email) > 254:
        return False, "Email too long (max 254 characters)"
    
    # Must have exactly one @
    if email.count('@') != 1:
        return False, "Email must contain exactly one @"
    
    local, domain = email.split('@')
    
    # Validate local part (before @)
    if not local or len(local) > 64:
        return False, "Local part invalid or too long (max 64 characters)"
    
    # Validate domain part
    if not domain or len(domain) > 253:
        return False, "Domain invalid or too long (max 253 characters)"
    
    # Domain must have at least one dot
    if '.' not in domain:
        return False, "Domain must contain at least one dot"
    
    # Check for valid characters in local part
    local_pattern = r'^[a-zA-Z0-9._+-]+$'
    if not re.match(local_pattern, local):
        return False, "Local part contains invalid characters"
    
    # Check for valid characters in domain
    domain_pattern = r'^[a-zA-Z0-9.-]+$'
    if not re.match(domain_pattern, domain):
        return False, "Domain contains invalid characters"
    
    # Domain parts can't start or end with hyphen
    domain_parts = domain.split('.')
    for part in domain_parts:
        if not part or part.startswith('-') or part.endswith('-'):
            return False, "Domain parts cannot start or end with hyphen"
    
    # TLD must be at least 2 characters
    if len(domain_parts[-1]) < 2:
        return False, "Top-level domain must be at least 2 characters"
    
    return True, "Valid email"


