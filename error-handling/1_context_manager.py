class DatabaseConnection:
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.conn = None
    
    def __enter__(self):
        try:
            print(f"Connecting to database: {self.connection_string}")
            # In reality, you'd use something like psycopg2 or SQLAlchemy here
            self.conn = "database_connection"
            return self
        except Exception as e:
            raise ConnectionError(f"Failed to connect: {str(e)}")
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing database connection")
        if self.conn:
            # Close connection here
            self.conn = None
        return False  # Don't suppress exceptions

# Usage
with DatabaseConnection("postgresql://localhost:5432/mydb") as db:
    # Do database operations
    # Connection is automatically closed after this block
    pass
  
