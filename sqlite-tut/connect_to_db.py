import sqlite3

# Connect to the db
with sqlite3.connect('example.db') as conn:
    cursor = conn.cursor()

    # Create customers table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            phone TEXT,
            num_orders INTEGER
        );
    ''')
    conn.commit()
    print("Customers table created successfully.")
    cursor.close()

