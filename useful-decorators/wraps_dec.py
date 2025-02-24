import functools

def log_execution(func):
    @functools.wraps(func)  # Preserves func's name, docstring, etc.
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper

@log_execution
def add(a, b):
    """Add two numbers and return the result."""
    return a + b

# Without @wraps, help(add) would show wrapper's info
help(add)  # Shows the original docstring
print(f"Function name: {add.__name__}")  # Shows "add", not "wrapper"

result = add(5, 3)
