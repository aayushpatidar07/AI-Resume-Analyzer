"""
Decorators Module
Utility decorators for the application
"""

from functools import wraps
from typing import Callable, Any
import logging
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)


def handle_errors(func: Callable) -> Callable:
    """
    Decorator to handle and log errors in functions
    
    Args:
        func: Function to decorate
        
    Returns:
        Decorated function with error handling
    """
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(f"Error in {func.__name__}: {str(e)}", exc_info=True)
            raise
    return wrapper


def validate_input(required_fields: list) -> Callable:
    """
    Decorator to validate required input fields
    
    Args:
        required_fields: List of required field names
        
    Returns:
        Decorator function
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(data: dict, *args: Any, **kwargs: Any) -> Any:
            missing = [field for field in required_fields if field not in data]
            if missing:
                raise ValueError(f"Missing required fields: {', '.join(missing)}")
            return func(data, *args, **kwargs)
        return wrapper
    return decorator


def cache_result(ttl_seconds: int = 300) -> Callable:
    """
    Decorator to cache function results with TTL (Time To Live)
    
    Args:
        ttl_seconds: Cache lifetime in seconds (default: 300)
        
    Returns:
        Decorator function
    """
    def decorator(func: Callable) -> Callable:
        cache = {}
        cache_times = {}
        
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            # Create cache key from args and kwargs
            cache_key = (args, tuple(sorted(kwargs.items())))
            
            # Check if result is cached and not expired
            if cache_key in cache:
                cached_time = cache_times.get(cache_key)
                if cached_time and (datetime.now() - cached_time) < timedelta(seconds=ttl_seconds):
                    logger.debug(f"Cache hit for {func.__name__}")
                    return cache[cache_key]
                else:
                    del cache[cache_key]
                    del cache_times[cache_key]
            
            # Call function and cache result
            result = func(*args, **kwargs)
            cache[cache_key] = result
            cache_times[cache_key] = datetime.now()
            logger.debug(f"Cached result for {func.__name__} (TTL: {ttl_seconds}s)")
            
            return result
        
        return wrapper
    return decorator
