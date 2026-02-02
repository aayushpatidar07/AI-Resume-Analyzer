"""
Request Context Management

Provides request-scoped context storage for tracking request metadata,
user information, and request-specific data throughout the application.
"""

from contextvars import ContextVar
from typing import Dict, Any, Optional
import uuid
from datetime import datetime


# Context variables
request_context: ContextVar[Optional[Dict[str, Any]]] = ContextVar(
    'request_context', 
    default=None
)


class RequestContext:
    """Manages request-scoped context information."""
    
    def __init__(self, request_id: Optional[str] = None):
        self.request_id = request_id or str(uuid.uuid4())
        self.timestamp = datetime.utcnow()
        self.user_id: Optional[str] = None
        self.metadata: Dict[str, Any] = {}
        self.tags: list = []
        
    def set_user(self, user_id: str) -> None:
        """Set the user ID for this request."""
        self.user_id = user_id
        
    def add_metadata(self, key: str, value: Any) -> None:
        """Add metadata to the context."""
        self.metadata[key] = value
        
    def add_tag(self, tag: str) -> None:
        """Add a tag to the context."""
        if tag not in self.tags:
            self.tags.append(tag)
            
    def to_dict(self) -> Dict[str, Any]:
        """Convert context to dictionary."""
        return {
            'request_id': self.request_id,
            'timestamp': self.timestamp.isoformat(),
            'user_id': self.user_id,
            'metadata': self.metadata,
            'tags': self.tags,
        }


def get_request_context() -> Optional[RequestContext]:
    """Get the current request context."""
    return request_context.get()


def set_request_context(ctx: RequestContext) -> None:
    """Set the current request context."""
    request_context.set(ctx)


def create_request_context(request_id: Optional[str] = None) -> RequestContext:
    """Create and set a new request context."""
    ctx = RequestContext(request_id)
    set_request_context(ctx)
    return ctx


def clear_request_context() -> None:
    """Clear the current request context."""
    request_context.set(None)
