"""
Audit Logging Module
Track all important actions for compliance
"""

from typing import Dict, Any, Optional
from datetime import datetime
from enum import Enum
import logging
import json

logger = logging.getLogger(__name__)


class AuditAction(Enum):
    """Audit action types"""
    ANALYSIS_STARTED = "analysis_started"
    ANALYSIS_COMPLETED = "analysis_completed"
    FILE_UPLOADED = "file_uploaded"
    FILE_DELETED = "file_deleted"
    USER_LOGIN = "user_login"
    USER_LOGOUT = "user_logout"
    CONFIGURATION_CHANGED = "config_changed"
    ERROR_OCCURRED = "error_occurred"


class AuditLog:
    """Audit log entry"""
    
    def __init__(self, action: AuditAction, user_id: Optional[str] = None,
                 details: Optional[Dict[str, Any]] = None):
        """
        Initialize audit log entry
        
        Args:
            action: Action type
            user_id: User performing action
            details: Additional details
        """
        self.id = None
        self.action = action
        self.user_id = user_id
        self.details = details or {}
        self.timestamp = datetime.now()
        self.ip_address = None
        self.user_agent = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return {
            'id': self.id,
            'action': self.action.value,
            'user_id': self.user_id,
            'details': self.details,
            'timestamp': self.timestamp.isoformat(),
            'ip_address': self.ip_address,
            'user_agent': self.user_agent
        }


class AuditLogger:
    """Manage audit logs"""
    
    def __init__(self):
        self.logs: list[AuditLog] = []
    
    def log_action(self, action: AuditAction,
                  user_id: Optional[str] = None,
                  details: Optional[Dict[str, Any]] = None,
                  ip_address: Optional[str] = None) -> AuditLog:
        """
        Log an action
        
        Args:
            action: Action type
            user_id: User ID
            details: Additional details
            ip_address: Client IP address
            
        Returns:
            Created audit log
        """
        log = AuditLog(action, user_id, details)
        log.ip_address = ip_address
        self.logs.append(log)
        
        logger.info(f"Audit: {action.value} by {user_id}")
        return log
    
    def log_analysis(self, user_id: Optional[str] = None,
                    match_percentage: float = 0.0,
                    file_size: int = 0) -> AuditLog:
        """
        Log analysis action
        
        Args:
            user_id: User ID
            match_percentage: Analysis result
            file_size: Resume file size
            
        Returns:
            Created audit log
        """
        return self.log_action(
            AuditAction.ANALYSIS_COMPLETED,
            user_id,
            {
                'match_percentage': match_percentage,
                'file_size': file_size
            }
        )
    
    def log_error(self, error_message: str,
                 user_id: Optional[str] = None,
                 context: Optional[Dict] = None) -> AuditLog:
        """
        Log error occurrence
        
        Args:
            error_message: Error message
            user_id: User ID
            context: Error context
            
        Returns:
            Created audit log
        """
        return self.log_action(
            AuditAction.ERROR_OCCURRED,
            user_id,
            {
                'error': error_message,
                'context': context or {}
            }
        )
    
    def get_logs_for_user(self, user_id: str) -> list[AuditLog]:
        """
        Get audit logs for user
        
        Args:
            user_id: User ID
            
        Returns:
            List of audit logs
        """
        return [log for log in self.logs if log.user_id == user_id]
    
    def get_logs_by_action(self, action: AuditAction) -> list[AuditLog]:
        """
        Get logs for specific action
        
        Args:
            action: Action type
            
        Returns:
            List of audit logs
        """
        return [log for log in self.logs if log.action == action]
    
    def export_logs(self, format: str = 'json') -> str:
        """
        Export audit logs
        
        Args:
            format: Export format (json or csv)
            
        Returns:
            Exported logs
        """
        if format == 'json':
            return json.dumps([log.to_dict() for log in self.logs], indent=2)
        elif format == 'csv':
            # CSV export implementation
            return "timestamp,action,user_id,details\n"
        return ""


# Global audit logger
audit_logger = AuditLogger()
