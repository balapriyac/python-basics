import sqlite3

# Connect to the db
with sqlite3.connect('example.db') as conn:
    cursor = conn.cursor()

    # Fetch and display all customers
    cursor.execute('SELECT id, first_name, last_name, email, num_orders FROM customers')
    all_customers = cursor.fetchall()
    print("All Customers:")
    for customer in all_customers:
        print(customer)

    # Update num_orders for a specific customer
    if all_customers:
        customer_id = all_customers[0][0]  # Take the ID of the first customer 
        new_num_orders = all_customers[0][4] + 1  # Increment num_orders by 1
        cursor.execute('''
            UPDATE customers
            SET num_orders = ?
            WHERE id = ?
        ''', (new_num_orders, customer_id))
        print(f"Orders updated for customer ID {customer_id}: now has {new_num_orders} orders.")
    
    conn.commit()
    cursor.close()
