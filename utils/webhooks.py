"""
Webhook Module
Support for webhooks to external services
"""

from typing import Dict, List, Optional, Any, Callable
import logging
import requests
from enum import Enum

logger = logging.getLogger(__name__)


class WebhookEvent(Enum):
    """Webhook event types"""
    ANALYSIS_COMPLETE = "analysis.complete"
    ERROR_OCCURRED = "error.occurred"
    BATCH_PROCESSING = "batch.processing"
    USER_SIGNUP = "user.signup"


class Webhook:
    """Webhook configuration"""
    
    def __init__(self, url: str, events: List[WebhookEvent],
                 secret: Optional[str] = None, active: bool = True):
        """
        Initialize webhook
        
        Args:
            url: Webhook URL
            events: List of events to trigger on
            secret: Secret for HMAC verification
            active: Whether webhook is active
        """
        self.id = None
        self.url = url
        self.events = events
        self.secret = secret
        self.active = active
        self.created_at = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return {
            'id': self.id,
            'url': self.url,
            'events': [e.value for e in self.events],
            'active': self.active
        }


class WebhookManager:
    """Manage webhooks"""
    
    def __init__(self):
        self.webhooks: List[Webhook] = []
    
    def register_webhook(self, url: str, events: List[WebhookEvent],
                        secret: Optional[str] = None) -> Webhook:
        """
        Register a webhook
        
        Args:
            url: Webhook URL
            events: Events to subscribe to
            secret: Optional webhook secret
            
        Returns:
            Registered webhook
        """
        webhook = Webhook(url, events, secret)
        self.webhooks.append(webhook)
        logger.info(f"Webhook registered: {url}")
        return webhook
    
    def unregister_webhook(self, webhook_id: int) -> bool:
        """
        Unregister a webhook
        
        Args:
            webhook_id: Webhook ID
            
        Returns:
            True if unregistered
        """
        for i, webhook in enumerate(self.webhooks):
            if webhook.id == webhook_id:
                del self.webhooks[i]
                logger.info(f"Webhook unregistered: {webhook_id}")
                return True
        return False
    
    def trigger_event(self, event: WebhookEvent, data: Dict[str, Any]) -> None:
        """
        Trigger an event for all registered webhooks
        
        Args:
            event: Event type
            data: Event data
        """
        for webhook in self.webhooks:
            if not webhook.active:
                continue
            
            if event not in webhook.events:
                continue
            
            try:
                response = requests.post(
                    webhook.url,
                    json={
                        'event': event.value,
                        'data': data
                    },
                    timeout=10
                )
                
                if response.status_code == 200:
                    logger.debug(f"Webhook delivered: {webhook.url}")
                else:
                    logger.warning(f"Webhook failed: {webhook.url} - {response.status_code}")
                    
            except Exception as e:
                logger.error(f"Webhook error: {webhook.url} - {str(e)}")
    
    def get_webhooks_for_event(self, event: WebhookEvent) -> List[Webhook]:
        """
        Get webhooks for specific event
        
        Args:
            event: Event type
            
        Returns:
            List of webhooks
        """
        return [w for w in self.webhooks 
                if w.active and event in w.events]
    
    def disable_webhook(self, webhook_id: int) -> bool:
        """
        Disable a webhook
        
        Args:
            webhook_id: Webhook ID
            
        Returns:
            True if disabled
        """
        for webhook in self.webhooks:
            if webhook.id == webhook_id:
                webhook.active = False
                logger.info(f"Webhook disabled: {webhook_id}")
                return True
        return False


# Global webhook manager
webhook_manager = WebhookManager()
