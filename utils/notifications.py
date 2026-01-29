"""
Notification System
Send notifications to users
"""

from typing import List, Dict, Any, Optional
from enum import Enum
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


class NotificationType(Enum):
    """Notification type enumeration"""
    INFO = "info"
    SUCCESS = "success"
    WARNING = "warning"
    ERROR = "error"


class Notification:
    """Notification model"""
    
    def __init__(self, 
                 title: str,
                 message: str,
                 notification_type: NotificationType = NotificationType.INFO,
                 user_id: Optional[str] = None):
        self.id = None
        self.title = title
        self.message = message
        self.type = notification_type
        self.user_id = user_id
        self.created_at = datetime.now()
        self.read = False
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return {
            'id': self.id,
            'title': self.title,
            'message': self.message,
            'type': self.type.value,
            'user_id': self.user_id,
            'created_at': self.created_at.isoformat(),
            'read': self.read
        }


class NotificationManager:
    """Manage notifications"""
    
    def __init__(self):
        self.notifications: List[Notification] = []
    
    def create_notification(self,
                           title: str,
                           message: str,
                           notification_type: NotificationType = NotificationType.INFO,
                           user_id: Optional[str] = None) -> Notification:
        """
        Create a notification
        
        Args:
            title: Notification title
            message: Notification message
            notification_type: Type of notification
            user_id: User ID (optional)
            
        Returns:
            Created notification
        """
        notification = Notification(title, message, notification_type, user_id)
        self.notifications.append(notification)
        logger.info(f"Notification created: {title}")
        return notification
    
    def mark_as_read(self, notification_id: int) -> bool:
        """
        Mark notification as read
        
        Args:
            notification_id: ID of notification
            
        Returns:
            True if successful
        """
        for notif in self.notifications:
            if notif.id == notification_id:
                notif.read = True
                return True
        return False
    
    def get_user_notifications(self, user_id: str) -> List[Notification]:
        """
        Get notifications for user
        
        Args:
            user_id: User ID
            
        Returns:
            List of notifications
        """
        return [n for n in self.notifications if n.user_id == user_id]
    
    def get_unread_count(self, user_id: str) -> int:
        """
        Get unread notification count
        
        Args:
            user_id: User ID
            
        Returns:
            Count of unread notifications
        """
        notifications = self.get_user_notifications(user_id)
        return sum(1 for n in notifications if not n.read)


# Global notification manager
notification_manager = NotificationManager()
