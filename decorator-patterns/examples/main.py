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
