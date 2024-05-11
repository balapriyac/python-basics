import sqlite3

# Define the threshold for the number of orders
order_threshold = 10

with sqlite3.connect('example.db') as conn:
    cursor = conn.cursor()

    # Fetch customers with less than 10 orders
    cursor.execute('''
        SELECT id, first_name, last_name, email, num_orders
        FROM customers
        WHERE num_orders < ?
    ''', (order_threshold,))

    # Fetch all matching customers
    filtered_customers = cursor.fetchall()

    # Display filtered customers
    if filtered_customers:
        print("Customers with less than 10 orders:")
        for customer in filtered_customers:
            print(customer)
    else:
        print("No customers found with less than 10 orders.")
