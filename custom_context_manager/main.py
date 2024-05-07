import sqlite3
from typing import Optional

# Writing a context manager class
class ConnectionManager:
    def __init__(self, db_name: str):
        self.db_name = db_name
        self.conn: Optional[sqlite3.Connection] = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        return self.conn

    def __exit__(self, exc_type, exc_value, traceback):
        if self.conn:
            self.conn.close()

# Example usage
db_name = "library.db"

# Using ConnectionManager context manager directly
with ConnectionManager(db_name) as conn:
    cursor = conn.cursor()

    # Create a books table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            title TEXT,
            author TEXT,
            publication_year INTEGER
        )
    """)

    # Insert sample book records
    books_data = [
        ("The Great Gatsby", "F. Scott Fitzgerald", 1925),
        ("To Kill a Mockingbird", "Harper Lee", 1960),
        ("1984", "George Orwell", 1949),
        ("Pride and Prejudice", "Jane Austen", 1813)
    ]
    cursor.executemany("INSERT INTO books (title, author, publication_year) VALUES (?, ?, ?)", books_data)
    conn.commit()

    # Retrieve and print all book records
    cursor.execute("SELECT * FROM books")
    records = cursor.fetchall()
    print("Library Catalog:")
    for record in records:
        book_id, title, author, publication_year = record
        print(f"Book ID: {book_id}, Title: {title}, Author: {author}, Year: {publication_year}")

