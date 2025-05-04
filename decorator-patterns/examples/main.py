def memoize(func):
    """Caches the return value of a function based on its arguments."""
    cache = {}

    def wrapper(*args, **kwargs):
        # Create a key that uniquely identifies the function call
        key = str(args) + str(kwargs)

        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]

    return wrapper

@memoize
def fibonacci(n):
    """Calculate the nth Fibonacci number."""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Without memoization, this would be painfully slow
result = fibonacci(50)  # Returns almost instantly instead of taking forever
print(f"The 50th Fibonacci number is {result}")

import logging
import functools

def log_calls(func=None, level=logging.INFO):
    """Log function calls with arguments and return values."""

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            args_str = ", ".join([str(a) for a in args])
            kwargs_str = ", ".join([f"{k}={v}" for k, v in kwargs.items()])
            all_args = f"{args_str}{', ' if args_str and kwargs_str else ''}{kwargs_str}"

            logging.log(level, f"Calling {func.__name__}({all_args})")
            result = func(*args, **kwargs)
            logging.log(level, f"{func.__name__} returned {result}")

            return result
        return wrapper

    # Handle both @log_calls and @log_calls(level=logging.DEBUG)
    if func is None:
        return decorator
    return decorator(func)

logging.basicConfig(level=logging.INFO)

@log_calls
def divide(a, b):
    return a / b

# This will log the call and the return value
result = divide(10, 2)

# You can also customize the logging level
@log_calls(level=logging.DEBUG)
def multiply(a, b):
    return a * b

result = multiply(5, 4)

import time
import functools

def timeit(func):
    """Measure and print the execution time of a function."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        print(f"{func.__name__} took {end_time - start_time:.4f} seconds to run")
        return result

    return wrapper

@timeit
def slow_function():
    """A deliberately slow function for demonstration."""
    total = 0
    for i in range(10000000):
        total += i
    return total

result = slow_function()  # Will print execution time

@timeit
def slow_function():
    """A deliberately slow function for demonstration."""
    total = 0
    for i in range(10000000):
        total += i
    return total

result = slow_function()  # Will print execution time

def retry(max_attempts=3, delay_seconds=1, backoff_factor=2, exceptions=(Exception,)):
    """Retry a function if it raises specified exceptions."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            current_delay = delay_seconds

            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    attempts += 1
                    if attempts == max_attempts:
                        logging.error(f"Failed after {attempts} attempts. Last error: {e}")
                        raise

                    logging.warning(
                        f"Attempt {attempts} failed with error: {e}. "
                        f"Retrying in {current_delay} seconds..."
                    )

                    time.sleep(current_delay)
                    current_delay *= backoff_factor

        return wrapper
    return decorator
    
import random
import requests

@retry(max_attempts=5, delay_seconds=1, exceptions=(requests.RequestException,))
def fetch_data(url):
    """Fetch data from an API with retry logic."""
    response = requests.get(url, timeout=2)
    response.raise_for_status()  # Raise exception for 4XX/5XX responses
    return response.json()

# This will retry up to 5 times if the request fails
try:
    data = fetch_data('https://api.example.com/data')
    print("Successfully fetched data!")
except Exception as e:
    print(f"All retry attempts failed: {e}")

def validate_positive_ints(func):
    def wrapper(*args):
        for arg in args:
            if not isinstance(arg, int) or arg <= 0:
                raise ValueError(f"{arg} must be a positive integer")
        return func(*args)
    return wrapper

@validate_positive_ints
def calculate_area(length, width):
    return length * width

print(calculate_area(5, 10))
print(calculate_area(-1, 10))
