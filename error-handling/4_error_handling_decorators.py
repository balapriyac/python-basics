from functools import wraps
import logging

def handle_api_errors(retries=3, fallback_value=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    logging.error(
                        f"API call failed (attempt {attempt + 1}/{retries}): {str(e)}"
                    )
                    if attempt == retries - 1:
                        if fallback_value is not None:
                            return fallback_value
                        raise
                except Exception as e:
                    logging.error(f"Unexpected error: {str(e)}")
                    raise
            return wrapper
        return decorator

# Usage
@handle_api_errors(retries=3, fallback_value=[])
def fetch_user_data(user_id):
    # Make API call here
    pass
  
