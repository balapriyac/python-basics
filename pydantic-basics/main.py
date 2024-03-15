import json
from pydantic import BaseModel, EmailStr, ValidationError, validator


class Employee(BaseModel):
    name: str
    age: int
    email: EmailStr
    department: str
    employee_id: str

    @validator("employee_id")
    def validate_employee_id(cls, v):
        if not v.isalnum() or len(v) != 6:
            raise ValueError("Employee ID must be exactly 6 alphanumeric characters")
        return v


# Load and parse the JSON data
with open("employees.json", "r") as f:
    data = json.load(f)

# Validate each employee record
for record in data:
    try:
        employee = Employee(**record)
        print(f"Valid employee record: {employee.name}")
    except ValidationError as e:
        print(f"Invalid employee record: {record['name']}")
        print(f"Errors: {e.errors()}")
