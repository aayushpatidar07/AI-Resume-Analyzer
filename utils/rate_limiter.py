"""
Rate Limiting Module
Implement rate limiting for API endpoints
"""

from typing import Dict, Optional
from datetime import datetime, timedelta
import logging

logger = logging.getLogger(__name__)


class RateLimiter:
    """Rate limiter for API endpoints"""
    
    def __init__(self, requests_per_minute: int = 60):
        """
        Initialize rate limiter
        
        Args:
            requests_per_minute: Maximum requests per minute
        """
        self.requests_per_minute = requests_per_minute
        self.request_history: Dict[str, list] = {}
    
    def is_allowed(self, identifier: str) -> bool:
        """
        Check if request is allowed
        
        Args:
            identifier: User ID or IP address
            
        Returns:
            True if request allowed
        """
        now = datetime.now()
        minute_ago = now - timedelta(minutes=1)
        
        if identifier not in self.request_history:
            self.request_history[identifier] = []
        
        # Remove old requests
        self.request_history[identifier] = [
            req_time for req_time in self.request_history[identifier]
            if req_time > minute_ago
        ]
        
        # Check limit
        if len(self.request_history[identifier]) >= self.requests_per_minute:
            logger.warning(f"Rate limit exceeded for {identifier}")
            return False
        
        # Add current request
        self.request_history[identifier].append(now)
        return True
    
    def get_remaining(self, identifier: str) -> int:
        """
        Get remaining requests for identifier
        
        Args:
            identifier: User ID or IP address
            
        Returns:
            Number of remaining requests
        """
        if identifier not in self.request_history:
            return self.requests_per_minute
        
        now = datetime.now()
        minute_ago = now - timedelta(minutes=1)
        
        requests = [
            req_time for req_time in self.request_history[identifier]
            if req_time > minute_ago
        ]
        
        return max(0, self.requests_per_minute - len(requests))
    
    def reset(self, identifier: str) -> None:
        """
        Reset rate limit for identifier
        
        Args:
            identifier: User ID or IP address
        """
        if identifier in self.request_history:
            del self.request_history[identifier]
            logger.debug(f"Rate limit reset for {identifier}")


class RateLimitConfig:
    """Rate limiting configuration"""
    
    # API endpoints rate limits
    ANALYZE_ENDPOINT = 30  # 30 requests per minute
    SAMPLE_DATA_ENDPOINT = 100  # 100 requests per minute
    BATCH_ENDPOINT = 10  # 10 requests per minute
    
    @staticmethod
    def get_limiter(endpoint: str, requests_per_minute: int = 60) -> RateLimiter:
        """
        Get rate limiter for endpoint
        
        Args:
            endpoint: Endpoint path
            requests_per_minute: Requests per minute limit
            
        Returns:
            RateLimiter instance
        """
        limiters = {
            '/analyze': RateLimiter(RateLimitConfig.ANALYZE_ENDPOINT),
            '/api/sample-data': RateLimiter(RateLimitConfig.SAMPLE_DATA_ENDPOINT),
            '/api/v2/batch-analyze': RateLimiter(RateLimitConfig.BATCH_ENDPOINT)
        }
        return limiters.get(endpoint, RateLimiter(requests_per_minute))
