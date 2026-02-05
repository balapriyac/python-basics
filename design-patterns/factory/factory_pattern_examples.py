"""
Factory Pattern Examples from the Tutorial
All code examples collected in one file for easy testing
"""

class EmailNotifier:
    def send(self, message):
        return f"Sending email: {message}"

class SMSNotifier:
    def send(self, message):
        return f"Sending SMS: {message}"

class PushNotifier:
    def send(self, message):
        return f"Sending push notification: {message}"

class NotificationFactory:
    @staticmethod
    def create_notifier(notifier_type):
        if notifier_type == "email":
            return EmailNotifier()
        elif notifier_type == "sms":
            return SMSNotifier()
        elif notifier_type == "push":
            return PushNotifier()
        else:
            raise ValueError(f"Unknown notifier type: {notifier_type}")

# Using the factory
notifier = NotificationFactory.create_notifier("email")
result = notifier.send("Hello, World!")
print(result)

class NotificationFactoryV2:
    notifier_types = {
        "email": EmailNotifier,
        "sms": SMSNotifier,
        "push": PushNotifier
    }
    
    @staticmethod
    def create_notifier(notifier_type):
        notifier_class = NotificationFactoryV2.notifier_types.get(notifier_type)
        if notifier_class:
            return notifier_class()
        else:
            raise ValueError(f"Unknown notifier type: {notifier_type}")

# Test with different types
email_notifier = NotificationFactoryV2.create_notifier("email")
sms_notifier = NotificationFactoryV2.create_notifier("sms")
push_notifier = NotificationFactoryV2.create_notifier("push")

print(email_notifier.send("Test email"))
print(sms_notifier.send("Test SMS"))
print(push_notifier.send("Test push"))

class PDFDocument:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.format = "PDF"
    
    def generate(self):
        return f"Generating {self.format}: '{self.title}' by {self.author}"

class WordDocument:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.format = "DOCX"
    
    def generate(self):
        return f"Generating {self.format}: '{self.title}' by {self.author}"

class MarkdownDocument:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.format = "MD"
    
    def generate(self):
        return f"Generating {self.format}: '{self.title}' by {self.author}"

class DocumentFactory:
    document_types = {
        "pdf": PDFDocument,
        "word": WordDocument,
        "markdown": MarkdownDocument
    }
    
    @staticmethod
    def create_document(doc_type, title, author):
        document_class = DocumentFactory.document_types.get(doc_type)
        if document_class:
            return document_class(title, author)
        else:
            raise ValueError(f"Unknown document type: {doc_type}")

# Create different documents with parameters
pdf = DocumentFactory.create_document("pdf", "Python Guide", "Tutorial Team")
word = DocumentFactory.create_document("word", "Meeting Notes", "John Smith")
markdown = DocumentFactory.create_document("markdown", "README", "DevTeam")

print(pdf.generate())
print(word.generate())
print(markdown.generate())

from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass
    
    @abstractmethod
    def refund(self, transaction_id):
        pass

class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing ${amount} via Credit Card"
    
    def refund(self, transaction_id):
        return f"Refunding credit card transaction {transaction_id}"

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing ${amount} via PayPal"
    
    def refund(self, transaction_id):
        return f"Refunding PayPal transaction {transaction_id}"

class CryptoProcessor(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing ${amount} via Cryptocurrency"
    
    def refund(self, transaction_id):
        return f"Refunding crypto transaction {transaction_id}"

class PaymentFactory:
    processors = {
        "credit_card": CreditCardProcessor,
        "paypal": PayPalProcessor,
        "crypto": CryptoProcessor
    }
    
    @staticmethod
    def create_processor(processor_type):
        processor_class = PaymentFactory.processors.get(processor_type)
        if processor_class:
            return processor_class()
        else:
            raise ValueError(f"Unknown processor type: {processor_type}")

# Use the factory
processor = PaymentFactory.create_processor("paypal")
print(processor.process_payment(99.99))
print(processor.refund("TXN12345"))

class MySQLConnection:
    def __init__(self, host, database):
        self.host = host
        self.database = database
        self.connection_type = "MySQL"
    
    def connect(self):
        return f"Connected to {self.connection_type} at {self.host}/{self.database}"
    
    def execute_query(self, query):
        return f"Executing on MySQL: {query}"

class PostgreSQLConnection:
    def __init__(self, host, database):
        self.host = host
        self.database = database
        self.connection_type = "PostgreSQL"
    
    def connect(self):
        return f"Connected to {self.connection_type} at {self.host}/{self.database}"
    
    def execute_query(self, query):
        return f"Executing on PostgreSQL: {query}"

class SQLiteConnection:
    def __init__(self, host, database):
        self.host = host
        self.database = database
        self.connection_type = "SQLite"
    
    def connect(self):
        return f"Connected to {self.connection_type} at {self.host}/{self.database}"
    
    def execute_query(self, query):
        return f"Executing on SQLite: {query}"

class DatabaseFactory:
    db_types = {
        "mysql": MySQLConnection,
        "postgresql": PostgreSQLConnection,
        "sqlite": SQLiteConnection
    }
    
    @staticmethod
    def create_connection(db_type, host, database):
        db_class = DatabaseFactory.db_types.get(db_type)
        if db_class:
            return db_class(host, database)
        else:
            raise ValueError(f"Unknown database type: {db_type}")
    
    @staticmethod
    def create_from_config(config):
        """Create a database connection from a configuration dictionary"""
        return DatabaseFactory.create_connection(
            config["type"],
            config["host"],
            config["database"]
        )

# Use with direct parameters
db1 = DatabaseFactory.create_connection("mysql", "localhost", "myapp_db")
print(db1.connect())
print(db1.execute_query("SELECT * FROM users"))

# Use with configuration dictionary
config = {
    "type": "postgresql",
    "host": "db.example.com",
    "database": "production_db"
}
db2 = DatabaseFactory.create_from_config(config)
print(db2.connect())
