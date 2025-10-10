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
