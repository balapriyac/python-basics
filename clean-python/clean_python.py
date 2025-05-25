def process_user(user_dict):
    if user_dict['status'] == 'active':  # What if 'status' is missing?
        send_email(user_dict['email'])   # What if it's 'mail' in some places?
        
        # Is it 'name', 'full_name', or 'username'? Who knows!
        log_activity(f"Processed {user_dict['name']}")


from dataclasses import dataclass
from typing import Optional

@dataclass
class User:
    id: int
    email: str
    full_name: str
    status: str
    last_login: Optional[datetime] = None

def process_user(user: User):
    if user.status == 'active':
        send_email(user.email)
        log_activity(f"Processed {user.full_name}")


def process_order(order, status):
    if status == 'pending':
        # process logic
    elif status == 'shipped':
        # different logic
    elif status == 'delivered':
        # more logic
    else:
        raise ValueError(f"Invalid status: {status}")
        
# Later in your code...
process_order(order, 'shiped')  # Typo! But no IDE warning

from enum import Enum, auto

class OrderStatus(Enum):
    PENDING = 'pending'
    SHIPPED = 'shipped'
    DELIVERED = 'delivered'
    
def process_order(order, status: OrderStatus):
    if status == OrderStatus.PENDING:
        # process logic
    elif status == OrderStatus.SHIPPED:
        # different logic
    elif status == OrderStatus.DELIVERED:
        # more logic
    
# Later in your code...
process_order(order, OrderStatus.SHIPPED)  # IDE autocomplete helps!

def create_user(name, email, admin=False, notify=True, temporary=False):
    # Implementation
    
# Later in code...
create_user("John Smith", "john@example.com", True, False)

def create_user(name, email, *, admin=False, notify=True, temporary=False):
    # Implementation

# Now you must use keywords for optional args
create_user("John Smith", "john@example.com", admin=True, notify=False)

import os

data_dir = os.path.join('data', 'processed')
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

filepath = os.path.join(data_dir, 'output.csv')
with open(filepath, 'w') as f:
    f.write('results\n')
    
# Check if we have a JSON file with the same name
json_path = os.path.splitext(filepath)[0] + '.json'
if os.path.exists(json_path):
    with open(json_path) as f:
        data = json.load(f)

from pathlib import Path

data_dir = Path('data') / 'processed'
data_dir.mkdir(parents=True, exist_ok=True)

filepath = data_dir / 'output.csv'
filepath.write_text('results\n')

# Check if we have a JSON file with the same name
json_path = filepath.with_suffix('.json')
if json_path.exists():
    data = json.loads(json_path.read_text())

def process_payment(order, user):
    if order.is_valid:
        if user.has_payment_method:
            payment_method = user.get_payment_method()
            if payment_method.has_sufficient_funds(order.total):
                try:
                    payment_method.charge(order.total)
                    order.mark_as_paid()
                    send_receipt(user, order)
                    return True
                except PaymentError as e:
                    log_error(e)
                    return False
            else:
                log_error("Insufficient funds")
                return False
        else:
            log_error("No payment method")
            return False
    else:
        log_error("Invalid order")
        return False

def process_payment(order, user):
    # Guard clauses: check preconditions first
    if not order.is_valid:
        log_error("Invalid order")
        return False
        
    if not user.has_payment_method:
        log_error("No payment method")
        return False
    
    payment_method = user.get_payment_method()
    if not payment_method.has_sufficient_funds(order.total):
        log_error("Insufficient funds")
        return False
    
    # Main logic comes after all validations
    try:
        payment_method.charge(order.total)
        order.mark_as_paid()
        send_receipt(user, order)
        return True
    except PaymentError as e:
        log_error(e)
        return False

