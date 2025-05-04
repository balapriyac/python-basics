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

# API calls
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
