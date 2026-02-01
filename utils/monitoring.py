"""
Monitoring and Observability
Application health monitoring and metrics
"""

from typing import Dict, Any, List, Callable
from datetime import datetime, timedelta
import psutil
import logging
from collections import deque

logger = logging.getLogger(__name__)


class MetricsCollector:
    """Collect and track application metrics"""
    
    def __init__(self, max_samples: int = 100):
        self.request_times = deque(maxlen=max_samples)
        self.error_count = 0
        self.success_count = 0
        self.start_time = datetime.now()
    
    def record_request(self, duration_ms: float, success: bool):
        """Record API request metrics"""
        self.request_times.append(duration_ms)
        if success:
            self.success_count += 1
        else:
            self.error_count += 1
    
    def get_metrics(self) -> Dict[str, Any]:
        """Get aggregated metrics"""
        if not self.request_times:
            return {'message': 'No metrics available yet'}
        
        times_list = list(self.request_times)
        return {
            'avg_response_time_ms': sum(times_list) / len(times_list),
            'min_response_time_ms': min(times_list),
            'max_response_time_ms': max(times_list),
            'total_requests': len(times_list),
            'success_count': self.success_count,
            'error_count': self.error_count,
            'success_rate': (self.success_count / (self.success_count + self.error_count) * 100) if (self.success_count + self.error_count) > 0 else 0,
            'uptime_seconds': (datetime.now() - self.start_time).total_seconds()
        }


class HealthStatus:
    """Application health status"""
    
    def __init__(self):
        self.status = "healthy"
        self.checks: Dict[str, Any] = {}
        self.last_check = datetime.now()
        self.check_history: deque = deque(maxlen=50)
    
    def check_database(self) -> bool:
        """Check database connection"""
        try:
            # Database connection check
            self.checks['database'] = {'status': 'ok', 'timestamp': datetime.now().isoformat()}
            return True
        except Exception as e:
            self.checks['database'] = {'status': 'failed', 'error': str(e), 'timestamp': datetime.now().isoformat()}
            return False
    
    def check_memory(self) -> bool:
        """Check memory usage"""
        try:
            memory = psutil.virtual_memory()
            percent = memory.percent
            self.checks['memory'] = {
                'status': 'ok' if percent < 90 else 'warning',
                'percent': percent,
                'timestamp': datetime.now().isoformat()
            }
            return percent < 95
        except Exception as e:
            logger.error(f"Memory check failed: {str(e)}")
            return False
    
    def check_disk(self) -> bool:
        """Check disk space"""
        try:
            disk = psutil.disk_usage('/')
            percent = disk.percent
            self.checks['disk'] = {
                'status': 'ok' if percent < 90 else 'warning',
                'percent': percent
            }
            return percent < 95
        except Exception as e:
            logger.error(f"Disk check failed: {str(e)}")
            return False
    
    def run_all_checks(self) -> Dict[str, Any]:
        """Run all health checks"""
        db_ok = self.check_database()
        mem_ok = self.check_memory()
        disk_ok = self.check_disk()
        
        if db_ok and mem_ok and disk_ok:
            self.status = "healthy"
        elif db_ok:
            self.status = "degraded"
        else:
            self.status = "unhealthy"
        
        self.last_check = datetime.now()
        
        return {
            'status': self.status,
            'last_check': self.last_check.isoformat(),
            'checks': self.checks
        }
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return {
            'status': self.status,
            'checks': self.checks,
            'last_check': self.last_check.isoformat()
        }


class Metrics:
    """Application metrics"""
    
    def __init__(self):
        self.requests_total = 0
        self.requests_success = 0
        self.requests_error = 0
        self.average_response_time = 0
        self.total_processing_time = 0
    
    def increment_request(self) -> None:
        """Increment request count"""
        self.requests_total += 1
    
    def increment_success(self) -> None:
        """Increment success count"""
        self.requests_success += 1
    
    def increment_error(self) -> None:
        """Increment error count"""
        self.requests_error += 1
    
    def add_response_time(self, time_ms: float) -> None:
        """Add response time"""
        self.total_processing_time += time_ms
        self.average_response_time = self.total_processing_time / self.requests_total if self.requests_total > 0 else 0
    
    def get_metrics(self) -> Dict[str, Any]:
        """Get metrics summary"""
        return {
            'total_requests': self.requests_total,
            'successful_requests': self.requests_success,
            'failed_requests': self.requests_error,
            'success_rate': (self.requests_success / self.requests_total * 100) if self.requests_total > 0 else 0,
            'average_response_time_ms': round(self.average_response_time, 2)
        }


# Global instances
health_status = HealthStatus()
metrics = Metrics()
