import time
import functools
from typing import Callable, Type, Tuple

def retry_with_backoff(
    max_attempts: int = 3,
    base_delay: float = 1.0,
    exponential_base: float = 2.0,
    exceptions: Tuple[Type[Exception], ...] = (Exception,)
):
    """
    Retry a function with exponential backoff.

    Args:
        max_attempts: Maximum number of retry attempts
        base_delay: Initial delay in seconds
        exponential_base: Multiplier for delay (2.0 = double each time)
        exceptions: Tuple of exception types to catch and retry
    """
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None

            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e

                    if attempt < max_attempts - 1:
                        delay = base_delay * (exponential_base ** attempt)
                        print(f"Attempt {attempt + 1} failed: {e}")
                        print(f"Retrying in {delay:.1f} seconds...")
                        time.sleep(delay)
                    else:
                        print(f"All {max_attempts} attempts failed")

            raise last_exception

        return wrapper
    return decorator

import random

@retry_with_backoff(max_attempts=4, base_delay=0.5, exceptions=(ConnectionError,))
def fetch_user_data(user_id):
    """Simulate an unreliable API."""
    if random.random() < 0.6:  # 60% failure rate
        raise ConnectionError("Service temporarily unavailable")
    return {"id": user_id, "name": "Sara", "status": "active"}

# Watch it retry automatically
result = fetch_user_data(12345)
print(f"Success: {result}")

from typing import Any, Callable, Dict, List, Optional

class ValidationError(Exception):
    """Raised when validation fails."""
    def __init__(self, field: str, errors: List[str]):
        self.field = field
        self.errors = errors
        super().__init__(f"{field}: {', '.join(errors)}")


def validate_input(
    value: Any,
    field_name: str,
    rules: Dict[str, Callable[[Any], bool]],
    messages: Optional[Dict[str, str]] = None
) -> Any:
    """
    Validate input against multiple rules.

    Returns the value if valid, raises ValidationError otherwise.
    """
    if messages is None:
        messages = {}

    errors = []

    for rule_name, rule_func in rules.items():
        try:
            if not rule_func(value):
                error_msg = messages.get(
                    rule_name,
                    f"Failed validation rule: {rule_name}"
                )
                errors.append(error_msg)
        except Exception as e:
            errors.append(f"Validation error in {rule_name}: {str(e)}")

    if errors:
        raise ValidationError(field_name, errors)

    return value

# Reusable validation rules
def not_empty(value: str) -> bool:
    return bool(value and value.strip())

def min_length(min_len: int) -> Callable:
    return lambda value: len(str(value)) >= min_len

def max_length(max_len: int) -> Callable:
    return lambda value: len(str(value)) <= max_len

def in_range(min_val: float, max_val: float) -> Callable:
    return lambda value: min_val <= float(value) <= max_val

try:
    username = validate_input(
        "ab",
        "username",
        {
            "not_empty": not_empty,
            "min_length": min_length(3),
            "max_length": max_length(20),
        },
        messages={
            "not_empty": "Username cannot be empty",
            "min_length": "Username must be at least 3 characters",
            "max_length": "Username cannot exceed 20 characters",
        }
    )
    print(f"Valid username: {username}")
except ValidationError as e:
    print(f"Invalid: {e}")

from typing import Any, Optional, List, Union

def safe_get(
    data: dict,
    path: Union[str, List[str]],
    default: Any = None,
    separator: str = "."
) -> Any:
    """
    Safely get a value from a nested dictionary.

    Args:
        data: The dictionary to access
        path: Dot-separated path (e.g., "user.address.city") or list of keys
        default: Value to return if path doesn't exist
        separator: Character to split path string (default: ".")

    Returns:
        The value at the path, or default if not found
    """
    # Convert string path to list
    if isinstance(path, str):
        keys = path.split(separator)
    else:
        keys = path

    current = data

    for key in keys:
        try:
            # Handle list indices (convert string to int if numeric)
            if isinstance(current, list):
                try:
                    key = int(key)
                except (ValueError, TypeError):
                    return default

            current = current[key]

        except (KeyError, IndexError, TypeError):
            return default

    return current

def safe_set(
    data: dict,
    path: Union[str, List[str]],
    value: Any,
    separator: str = ".",
    create_missing: bool = True
) -> bool:
    """
    Safely set a value in a nested dictionary.

    Args:
        data: The dictionary to modify
        path: Dot-separated path or list of keys
        value: Value to set
        separator: Character to split path string
        create_missing: Whether to create missing intermediate dicts

    Returns:
        True if successful, False otherwise
    """
    if isinstance(path, str):
        keys = path.split(separator)
    else:
        keys = path

    if not keys:
        return False

    current = data

    # Navigate to the parent of the final key
    for key in keys[:-1]:
        if key not in current:
            if create_missing:
                current[key] = {}
            else:
                return False

        current = current[key]

        if not isinstance(current, dict):
            return False

    # Set the final value
    current[keys[-1]] = value
    return True

# Sample nested data
user_data = {
    "user": {
        "name": "Anna",
        "address": {
            "city": "San Francisco",
            "zip": "94105"
        },
        "orders": [
            {"id": 1, "total": 99.99},
            {"id": 2, "total": 149.50}
        ]
    }
}

# Safe get examples
city = safe_get(user_data, "user.address.city")
print(f"City: {city}")

country = safe_get(user_data, "user.address.country", default="Unknown")
print(f"Country: {country}")

first_order = safe_get(user_data, "user.orders.0.total")
print(f"First order: ${first_order}")

# Safe set example
new_data = {}
safe_set(new_data, "user.settings.theme", "dark")
print(f"Created: {new_data}")

import threading
import functools
from typing import Callable, Optional

class TimeoutError(Exception):
    """Raised when an operation exceeds its timeout."""
    pass

def timeout(seconds: int, error_message: Optional[str] = None):
    """
    Decorator to enforce a timeout on function execution.

    Args:
        seconds: Maximum execution time in seconds
        error_message: Custom error message for timeout
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = [TimeoutError(
                error_message or f"Operation timed out after {seconds} seconds"
            )]

            def target():
                try:
                    result[0] = func(*args, **kwargs)
                except Exception as e:
                    result[0] = e

            thread = threading.Thread(target=target)
            thread.daemon = True
            thread.start()
            thread.join(timeout=seconds)

            if thread.is_alive():
                raise TimeoutError(
                    error_message or f"Operation timed out after {seconds} seconds"
                )

            if isinstance(result[0], Exception):
                raise result[0]

            return result[0]

        return wrapper
    return decorator

import time

@timeout(2, error_message="Query took too long")
def slow_database_query():
    """Simulate a slow query."""
    time.sleep(5)
    return "Query result"

@timeout(3)
def fetch_data():
    """Simulate a quick operation."""
    time.sleep(1)
    return {"data": "value"}

# Test timeout
try:
    result = slow_database_query()
    print(f"Result: {result}")
except TimeoutError as e:
    print(f"Timeout: {e}")

# Test success
try:
    data = fetch_data()
    print(f"Success: {data}")
except TimeoutError as e:
    print(f"Timeout: {e}")

from contextlib import contextmanager
from typing import Callable, Any, Optional
import traceback

@contextmanager
def managed_resource(
    acquire: Callable[[], Any],
    release: Callable[[Any], None],
    on_error: Optional[Callable[[Exception, Any], None]] = None,
    suppress_errors: bool = False
):
    """
    Context manager for automatic resource acquisition and cleanup.

    Args:
        acquire: Function to acquire the resource
        release: Function to release the resource
        on_error: Optional error handler
        suppress_errors: Whether to suppress exceptions after cleanup
    """
    resource = None
    try:
        resource = acquire()
        yield resource
    except Exception as e:
        if on_error and resource is not None:
            try:
                on_error(e, resource)
            except Exception as handler_error:
                print(f"Error in error handler: {handler_error}")

        if not suppress_errors:
            raise
    finally:
        if resource is not None:
            try:
                release(resource)
            except Exception as cleanup_error:
                print(f"Error during cleanup: {cleanup_error}")
                traceback.print_exc()

class ResourceTracker:
    """Helper class to track resource operations."""

    def __init__(self, name: str, verbose: bool = True):
        self.name = name
        self.verbose = verbose
        self.operations = []

    def log(self, operation: str):
        self.operations.append(operation)
        if self.verbose:
            print(f"[{self.name}] {operation}")

    def acquire(self):
        self.log("Acquiring resource")
        return self

    def release(self):
        self.log("Releasing resource")

    def use(self, action: str):
        self.log(f"Using resource: {action}")

# Example: Operation with error handling
tracker = ResourceTracker("Database")

def error_handler(exception, resource):
    resource.log(f"Error occurred: {exception}")
    resource.log("Attempting rollback")

try:
    with managed_resource(
        acquire=lambda: tracker.acquire(),
        release=lambda r: r.release(),
        on_error=error_handler
    ) as db:
        db.use("INSERT INTO users")
        raise ValueError("Duplicate entry")
except ValueError as e:
    print(f"Caught: {e}")
