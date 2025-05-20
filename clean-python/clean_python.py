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

