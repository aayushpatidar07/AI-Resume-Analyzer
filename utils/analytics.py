"""
Analytics Module
Track and analyze application usage patterns
"""

from typing import Dict, List, Any
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


class AnalyticsTracker:
    """Track application analytics and metrics"""
    
    def __init__(self):
        self.events: List[Dict[str, Any]] = []
        self.sessions: Dict[str, Any] = {}
    
    def track_event(self, event_name: str, 
                   data: Dict[str, Any] = None,
                   user_id: str = None) -> None:
        """
        Track an event
        
        Args:
            event_name: Name of the event
            data: Additional event data
            user_id: User identifier
        """
        event = {
            'name': event_name,
            'timestamp': datetime.now().isoformat(),
            'data': data or {},
            'user_id': user_id
        }
        self.events.append(event)
        logger.debug(f"Event tracked: {event_name}")
    
    def track_resume_analysis(self, match_percentage: float,
                             resume_size: int,
                             processing_time: float) -> None:
        """
        Track resume analysis event
        
        Args:
            match_percentage: Match percentage result
            resume_size: Size of resume in bytes
            processing_time: Time taken to process
        """
        self.track_event('resume_analysis', {
            'match_percentage': match_percentage,
            'resume_size': resume_size,
            'processing_time': processing_time
        })
    
    def get_statistics(self) -> Dict[str, Any]:
        """
        Get analytics statistics
        
        Returns:
            Analytics statistics
        """
        total_events = len(self.events)
        event_types = {}
        
        for event in self.events:
            name = event['name']
            event_types[name] = event_types.get(name, 0) + 1
        
        return {
            'total_events': total_events,
            'event_types': event_types,
            'sessions_count': len(self.sessions)
        }


# Global analytics instance
analytics = AnalyticsTracker()
