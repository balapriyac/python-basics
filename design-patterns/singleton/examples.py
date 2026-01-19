class DatabaseConnection:
    """
    Classic Singleton pattern using __new__
    """
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Creating new database connection")
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        # Only initialize once
        if not self._initialized:
            print("Initializing database connection")
            self.connection_string = "postgresql://localhost/mydb"
            self.pool_size = 10
            self._initialized = True

    def query(self, sql):
        return f"Executing: {sql}"

# Test the singleton behavior
db1 = DatabaseConnection()
print(f"db1 connection: {db1.connection_string}")

print("\nCreating second instance:")
db2 = DatabaseConnection()
print(f"db2 connection: {db2.connection_string}")

print(f"\nAre they the same object? {db1 is db2}")

def singleton(cls):
    """
    Decorator that converts a class into a singleton
    """
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance

@singleton
class AppConfig:
    """
    Application configuration as a singleton
    """
    def __init__(self):
        print("Loading configuration...")
        self.debug_mode = True
        self.api_key = "secret-key-12345"
        self.max_connections = 100
        self.timeout = 30

    def update_setting(self, key, value):
        setattr(self, key, value)
        print(f"Updated {key} = {value}")

# First access
config1 = AppConfig()
print(f"Debug mode: {config1.debug_mode}")

# Second access - no re-initialization
print("\nAccessing config again:")
config2 = AppConfig()
config2.update_setting("timeout", 60)

print(f"\nconfig1 timeout: {config1.timeout}")
print(f"Same instance? {config1 is config2}")

class SingletonMeta(type):
    """
    Metaclass that creates singleton instances
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Logger(metaclass=SingletonMeta):
    """
    Simple logging singleton using metaclass
    """
    def __init__(self):
        self.logs = []

    def log(self, message):
        self.logs.append(message)
        print(f"[LOG] {message}")

    def get_logs(self):
        return self.logs

# Use the logger from different parts of code
logger1 = Logger()
logger1.log("Application started")
logger1.log("User logged in")

# Another part of code gets the same logger
logger2 = Logger()
logger2.log("Processing request")

print(f"\nTotal logs in logger1: {len(logger1.get_logs())}")
print(f"Total logs in logger2: {len(logger2.get_logs())}")
print(f"Same logger? {logger1 is logger2}")

import threading

class ThreadSafeSingleton:
    """
    Thread-safe singleton using a lock
    """
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                # Double-check pattern
                if cls._instance is None:
                    print(f"Thread {threading.current_thread().name}: Creating instance")
                    cls._instance = super().__new__(cls)
                    cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if not self._initialized:
            with self._lock:
                if not self._initialized:
                    print(f"Thread {threading.current_thread().name}: Initializing")
                    self.data = {}
                    self._initialized = True

# Test with multiple threads
def create_singleton(thread_id):
    instance = ThreadSafeSingleton()
    instance.data[thread_id] = f"Data from thread {thread_id}"

threads = []
for i in range(5):
    t = threading.Thread(target=create_singleton, args=(i,), name=f"Thread-{i}")
    threads.append(t)
    t.start()

for t in threads:
    t.join()

# Verify it's a singleton
final = ThreadSafeSingleton()
print(f"\nShared data across all threads: {final.data}")


