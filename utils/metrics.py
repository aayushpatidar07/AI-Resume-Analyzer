"""
Performance Metrics Module

Tracks and analyzes application performance metrics including
API response times, resource usage, and throughput analysis.
"""

from datetime import datetime, timedelta
from typing import Dict, List, Optional
from collections import defaultdict
import time


class PerformanceMetrics:
    """Track and analyze application performance metrics."""
    
    def __init__(self):
        self.metrics: Dict[str, List[float]] = defaultdict(list)
        self.start_times: Dict[str, float] = {}
        self.request_count = 0
        self.error_count = 0
        
    def start_timer(self, operation: str) -> None:
        """Start timing an operation."""
        self.start_times[operation] = time.time()
        
    def end_timer(self, operation: str) -> float:
        """End timing and record duration."""
        if operation in self.start_times:
            duration = time.time() - self.start_times[operation]
            self.metrics[operation].append(duration)
            del self.start_times[operation]
            return duration
        return 0.0
        
    def get_average(self, operation: str) -> float:
        """Get average duration for operation."""
        values = self.metrics.get(operation, [])
        return sum(values) / len(values) if values else 0.0
        
    def get_percentile(self, operation: str, percentile: int = 95) -> float:
        """Get percentile for operation."""
        values = sorted(self.metrics.get(operation, []))
        if not values:
            return 0.0
        index = int(len(values) * percentile / 100)
        return values[min(index, len(values) - 1)]
        
    def get_summary(self) -> Dict:
        """Get performance summary."""
        summary = {}
        for operation, values in self.metrics.items():
            summary[operation] = {
                'count': len(values),
                'avg': self.get_average(operation),
                'p95': self.get_percentile(operation, 95),
                'p99': self.get_percentile(operation, 99),
                'min': min(values) if values else 0,
                'max': max(values) if values else 0,
            }
        return summary


# Global metrics instance
performance_metrics = PerformanceMetrics()


def track_performance(operation_name: str):
    """Decorator to track performance of functions."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            performance_metrics.start_timer(operation_name)
            try:
                result = func(*args, **kwargs)
                return result
            finally:
                performance_metrics.end_timer(operation_name)
        return wrapper
    return decorator
