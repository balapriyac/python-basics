# memoization
import functools
from typing import Callable, Dict, Any, Tuple

def memoize(func: Callable) -> Callable:
    """Cache the results of a function call to avoid redundant computation."""
    cache: Dict[Tuple, Any] = {}
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Create a hashable key from the function arguments
        key = (*args, *(sorted(kwargs.items())))
        
        if key not in cache:
            cache[key] = func(*args, **kwargs)
            
        return cache[key]
    
    # Add a method to clear the cache if needed
    wrapper.clear_cache = lambda: cache.clear()
    
    return wrapper

# example: API calls
import requests
import time

@memoize
def fetch_user_data(user_id: int) -> dict:
    """Fetch user data from an external API."""
    print(f"Fetching data for user {user_id}...")
    # Simulate API request delay
    time.sleep(1)
    
    # This would be a real API call in production code
    response = requests.get(f"https://api.example.com/users/{user_id}")
    return response.json()

# Logging
import functools
import logging
from typing import Callable, Any, Optional

def log_calls(level: int = logging.DEBUG, logger: Optional[logging.Logger] = None):
    """
    Log function calls, arguments, and return values.
    
    Args:
        level: The logging level to use
        logger: A specific logger to use, if None will use the root logger
    """
    if logger is None:
        logger = logging.getLogger()
    
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            func_name = func.__name__
            arg_str = ", ".join([repr(a) for a in args] + 
                              [f"{k}={repr(v)}" for k, v in kwargs.items()])
            
            logger.log(level, f"Calling {func_name}({arg_str})")
            
            try:
                result = func(*args, **kwargs)
                logger.log(level, f"{func_name} returned: {repr(result)}")
                return result
            except Exception as e:
                logger.log(logging.ERROR, f"{func_name} raised: {repr(e)}")
                raise
                
        return wrapper
    
    # Handle case when decorator is used without parameters
    if callable(level):
        func, level = level, logging.DEBUG
        return decorator(func)
    
    return decorator
    
# Example: logging calls in data proc. pipeline
import logging

# Configure logging with a nice format
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Create a custom logger for our module
logger = logging.getLogger('data_pipeline')


@log_calls(logger=logger)
def parse_customer_record(record):
    """Extract customer information from a raw data record."""
    # Extract and validate customer ID
    customer_id = record.get('id')
    
    if not customer_id:
        raise ValueError("Missing customer ID in record")
        
    # Transform the raw data into our standardized format
    return {
        'customer_id': customer_id,
        'name': f"{record.get('first_name', '')} {record.get('last_name', '')}".strip(),
        'email': record.get('email', '').lower(),
        'signup_date': record.get('created_at')
    }

# Sample data - mix of valid and invalid records
records = [
    {'id': 101, 'first_name': 'Jane', 'last_name': 'Doe', 'email': 'JANE@example.com'},
    # Record missing the ID field will cause an error
    {'first_name': 'Alice', 'last_name': 'Johnson', 'email': 'alice@example.com'}
]

# Process each record
for record in records:
    try:
        processed = parse_customer_record(record)
        # Further processing would happen here
    except Exception as e:
        logger.error(f"Failed to process record: {record}")

# Timer
import functools
import time
from typing import Callable, Optional
import logging

def timer(func: Optional[Callable] = None, *, logger: Optional[logging.Logger] = None, 
          level: int = logging.INFO):
    """
    Measure and log the execution time of the decorated function.
    
    Args:
        func: The function to decorate
        logger: Logger to use (default: root logger)
        level: Logging level for the timer messages
    """
    # Use the root logger if none provided
    if logger is None:
        logger = logging.getLogger()
        
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Record the start time with high precision
            start_time = time.perf_counter()
            
            # Call the original function
            result = func(*args, **kwargs)
            
            # Calculate elapsed time
            end_time = time.perf_counter()
            elapsed_time = end_time - start_time
            
            # Log the execution time
            logger.log(level, f"{func.__name__} took {elapsed_time:.6f} seconds to run")
            
            return result
        return wrapper
    
    # Handle both @timer and @timer(logger=my_logger) syntax
    if func is None:
        return decorator
    else:
        return decorator(func)

# Example: data proc. functions
import logging
import time

# Set up a logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('performance')

# Create some sample data
data = [i for i in range(1000000)]

@timer(logger=logger)
def calculate_statistics(numbers):
    """Calculate basic statistics for a list of numbers."""
    # Simulate some processing time
    time.sleep(0.1)
    
    return {
        'min': min(numbers),
        'max': max(numbers),
        'avg': sum(numbers) / len(numbers)
    }

@timer(logger=logger)
def filter_outliers(numbers, threshold=2):
    """Filter out values that are far from the mean."""
    # Simulate more complex processing
    time.sleep(0.2)
    
    mean = sum(numbers) / len(numbers)
    return [n for n in numbers if abs(n - mean) < threshold]
