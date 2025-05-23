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

