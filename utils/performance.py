"""
Performance Monitoring
Track and analyze application performance metrics
"""

import time
import logging
from typing import Callable, Any, Dict
from functools import wraps
from datetime import datetime

logger = logging.getLogger(__name__)


class PerformanceMonitor:
    """Monitor application performance"""
    
    def __init__(self):
        self.metrics: Dict[str, Any] = {}
        self.start_time = datetime.now()
    
    def start_timer(self, key: str) -> None:
        """
        Start a performance timer
        
        Args:
            key: Timer identifier
        """
        self.metrics[key] = {
            'start': time.time(),
            'end': None,
            'duration': None
        }
    
    def stop_timer(self, key: str) -> float:
        """
        Stop a performance timer
        
        Args:
            key: Timer identifier
            
        Returns:
            Duration in seconds
        """
        if key not in self.metrics:
            logger.warning(f"Timer '{key}' not found")
            return 0
        
        end = time.time()
        duration = end - self.metrics[key]['start']
        self.metrics[key]['end'] = end
        self.metrics[key]['duration'] = duration
        
        logger.debug(f"Timer '{key}' completed in {duration:.4f}s")
        return duration
    
    def get_metric(self, key: str) -> Dict[str, Any]:
        """
        Get metric by key
        
        Args:
            key: Metric identifier
            
        Returns:
            Metric data
        """
        return self.metrics.get(key, {})
    
    def get_uptime(self) -> float:
        """
        Get application uptime in seconds
        
        Returns:
            Uptime in seconds
        """
        return (datetime.now() - self.start_time).total_seconds()
    
    def report(self) -> Dict[str, Any]:
        """
        Get performance report
        
        Returns:
            Performance report
        """
        return {
            'uptime_seconds': self.get_uptime(),
            'metrics_count': len(self.metrics),
            'metrics': self.metrics
        }


def measure_performance(func: Callable) -> Callable:
    """
    Decorator to measure function performance
    
    Args:
        func: Function to measure
        
    Returns:
        Decorated function
    """
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start = time.time()
        logger.debug(f"Starting {func.__name__}")
        
        try:
            result = func(*args, **kwargs)
            return result
        finally:
            duration = time.time() - start
            logger.info(f"{func.__name__} took {duration:.4f}s")
    
    return wrapper


def cache_with_ttl(ttl_seconds: int) -> Callable:
    """
    Decorator to cache results with TTL
    
    Args:
        ttl_seconds: Time-to-live in seconds
        
    Returns:
        Decorator function
    """
    def decorator(func: Callable) -> Callable:
        cache = {}
        cache_times = {}
        
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            # Create cache key
            key = f"{func.__name__}:{str(args)}:{str(kwargs)}"
            current_time = time.time()
            
            # Check cache
            if key in cache:
                cache_time = cache_times.get(key, 0)
                if current_time - cache_time < ttl_seconds:
                    logger.debug(f"Cache hit for {func.__name__}")
                    return cache[key]
                else:
                    del cache[key]
                    del cache_times[key]
            
            # Execute and cache
            result = func(*args, **kwargs)
            cache[key] = result
            cache_times[key] = current_time
            logger.debug(f"Cached {func.__name__}")
            
            return result
        
        return wrapper
    return decorator


# Global performance monitor
perf_monitor = PerformanceMonitor()
