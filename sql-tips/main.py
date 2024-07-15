import sqlite3
from faker import Faker
import random

# Initialize Faker
fake = Faker()

# Connect to SQLite database (or create it)
conn = sqlite3.connect('employees.db')
cursor = conn.cursor()

# Create employees table
cursor.execute('''
CREATE TABLE IF NOT EXISTS employees (
    employee_id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone_number TEXT,
    hire_date TEXT,
    job_id TEXT,
    salary REAL,
    department TEXT
)
''')

# Function to generate fake employee data
def generate_employee_data(num_records):
    employees = []
    for _ in range(num_records):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        phone_number = fake.phone_number()
        hire_date = fake.date_between(start_date='-10y', end_date='today').isoformat()
        job_id = random.choice(['IT_PROG', 'HR_REP', 'FIN_ANALYST', 'SALES_REP'])
        salary = round(random.uniform(30000, 120000), 2)
        department = random.choice(['IT', 'HR', 'Finance', 'Sales'])
        
        employees.append((first_name, last_name, email, phone_number, hire_date, job_id, salary, department))
    return employees

# Insert fake data into employees table
num_records = 1000
employee_data = generate_employee_data(num_records)
cursor.executemany('''
INSERT INTO employees (first_name, last_name, email, phone_number, hire_date, job_id, salary, department)
VALUES (?, ?, ?, ?, ?, ?, ?, ?)
''', employee_data)

# Commit changes and close connection
conn.commit()
conn.close()

print(f"Inserted {num_records} records into the employees table.")
