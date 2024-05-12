import sqlite3

# Specify the customer ID of the customer to delete
cid_to_delete = 3  

with sqlite3.connect('example.db') as conn:
    cursor = conn.cursor()

    # Execute DELETE statement to remove the customer with the specified ID
    cursor.execute('''
        DELETE FROM customers
        WHERE id = ?
    ''', (cid_to_delete,))

    print(f"Customer with ID {cid_to_delete} deleted successfully.")

    conn.commit()
    cursor.close()
