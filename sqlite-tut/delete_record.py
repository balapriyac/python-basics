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

    # Check the rowcount to determine if a customer was deleted
    if cursor.rowcount > 0:
        print(f"Customer with ID {cid_to_delete} deleted successfully.")
    else:
        print(f"No customer found with ID {cid_to_delete}.")


    conn.commit()
    cursor.close()
