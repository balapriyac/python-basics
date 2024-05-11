import sqlite3
import random
from faker import Faker

# Initialize Faker object
fake = Faker()
Faker.seed(24)

# Connect to the db
with sqlite3.connect('example.db') as conn:
    cursor = conn.cursor()

    # Insert customer records
    num_records = 10
    for _ in range(num_records):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        phone = fake.phone_number()
        num_orders = random.randint(0,100)

        cursor.execute('''
            INSERT INTO customers (first_name, last_name, email, phone, num_orders)
            VALUES (?, ?, ?, ?, ?)
        ''', (first_name, last_name, email, phone, num_orders))
    print(f"{num_records} customer records inserted successfully.")
    conn.commit()
    cursor.close()
