"""
Decorators Module
Utility decorators for the application
"""

from functools import wraps
from typing import Callable, Any
import logging

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
