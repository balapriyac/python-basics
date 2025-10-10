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
