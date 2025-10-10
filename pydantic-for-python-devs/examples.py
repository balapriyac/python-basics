# ! pip install pydantic

from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    email: str
# Create a user
user = User(name="Alice", age="25", email="alice@example.com")
print(user.age)
print(type(user.age))

from pydantic import BaseModel, Field
from typing import Optional

class Product(BaseModel):
    name: str
    price: float
    description: Optional[str] = None
    in_stock: bool = True
    category: str = Field(default="general", min_length=1)

# All these work
product1 = Product(name="Widget", price=9.99)
product2 = Product(name="Gadget", price=15.50, description="Useful tool")

from pydantic import BaseModel, field_validator
import re

class Account(BaseModel):
    username: str
    email: str
    password: str

    @field_validator('username')
    def validate_username(cls, v):
        if len(v) < 3:
            raise ValueError('Username must be at least 3 characters')
        if not v.isalnum():
            raise ValueError('Username must be alphanumeric')
        return v.lower()  # Normalize to lowercase

    @field_validator('email')
    def validate_email(cls, v):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(pattern, v):
            raise ValueError('Invalid email format')
        return v

    @field_validator('password')
    def validate_password(cls, v):
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters')
        return v

account = Account(
    username="JohnDoe123",
    email="john@example.com",
    password="secretpass123"
)

from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class Address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str

    @field_validator('zip_code')
    def validate_zip(cls, v):
        if not v.isdigit() or len(v) != 5:
            raise ValueError('ZIP code must be 5 digits')
        return v

class Contact(BaseModel):
    name: str
    phone: str
    email: Optional[str] = None

class Company(BaseModel):
    name: str
    founded: datetime
    address: Address
    contacts: List[Contact]
    employee_count: int
    is_public: bool = False

# Complex nested data gets fully validated
company_data = {
    "name": "Tech Corp",
    "founded": "2020-01-15T10:00:00",
    "address": {
        "street": "123 Main St",
        "city": "San Francisco",
        "state": "CA",
        "zip_code": "94105"
    },
    "contacts": [
        {"name": "John Smith", "phone": "555-0123"},
        {"name": "Jane Doe", "phone": "555-0456", "email": "jane@techcorp.com"}
    ],
    "employee_count": 150
}

company = Company(**company_data)


from pydantic import BaseModel, Field, field_validator
from typing import Union, Optional
from datetime import datetime
import json

class APIResponse(BaseModel):
    status: str
    message: Optional[str] = None
    data: Optional[dict] = None
    timestamp: datetime = Field(default_factory=datetime.now)

class UserProfile(BaseModel):
    id: int
    username: str
    full_name: Optional[str] = None
    age: Optional[int] = Field(None, ge=0, le=150)  # Age constraints
    created_at: Union[datetime, str]  # Handle multiple formats
    is_verified: bool = False

    @field_validator('created_at', mode='before')
    def parse_created_at(cls, v):
        if isinstance(v, str):
            try:
                return datetime.fromisoformat(v.replace('Z', '+00:00'))
            except ValueError:
                raise ValueError('Invalid datetime format')
        return v

# Simulate API response
api_json = '''
{
    "status": "success",
    "data": {
        "id": 123,
        "username": "alice_dev",
        "full_name": "Alice Johnson",
        "age": "28",
        "created_at": "2023-01-15T10:30:00Z",
        "is_verified": true
    }
}
'''

response_data = json.loads(api_json)
api_response = APIResponse(**response_data)

if api_response.data:
    user = UserProfile(**api_response.data)
    print(f"User {user.username} created at {user.created_at}")

from pydantic import BaseModel, ValidationError
from typing import List

class Order(BaseModel):
    order_id: int
    customer_email: str
    items: List[str]
    total: float

    @field_validator('total')
    def positive_total(cls, v):
        if v <= 0:
            raise ValueError('Total must be positive')
        return v

# Invalid data
bad_data = {
    "order_id": "not_a_number",
    "customer_email": "invalid_email",
    "items": "should_be_list",
    "total": -10.50
}

try:
    order = Order(**bad_data)
except ValidationError as e:
    print("Validation errors:")
    for error in e.errors():
        field = error['loc'][0]
        message = error['msg']
        print(f"  {field}: {message}")

    # Get JSON representation of errors
    print("\nJSON errors:")
    print(e.json(indent=2))


from pydantic import BaseModel
from datetime import datetime

class Event(BaseModel):
    name: str
    date: datetime
    attendees: int
    is_public: bool = True

event = Event(
    name="Python Meetup",
    date=datetime(2024, 3, 15, 18, 30),
    attendees=45
)

# Export to dictionary
event_dict = event.model_dump()
print(event_dict)

# Export to JSON string
event_json = event.model_dump_json()
print(event_json)

# Export with exclusions
public_data = event.model_dump(exclude={'attendees'})
print(public_data)

# Export with custom serialization
formatted_json = event.model_dump_json(indent=2)
print(formatted_json)

