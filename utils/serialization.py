"""
Data Serialization Module

Provides utilities for serializing and deserializing complex data types
including dates, decimals, and custom objects.
"""

import json
from datetime import datetime, date
from decimal import Decimal
from typing import Any, Dict, Type
from uuid import UUID


class DataSerializer:
    """Handle serialization of complex data types."""
    
    @staticmethod
    def to_json(data: Any, **kwargs) -> str:
        """Serialize data to JSON string."""
        return json.dumps(data, cls=CustomJSONEncoder, **kwargs)
    
    @staticmethod
    def from_json(json_str: str) -> Any:
        """Deserialize JSON string to Python object."""
        return json.loads(json_str)
    
    @staticmethod
    def to_dict(obj: Any) -> Dict[str, Any]:
        """Convert object to dictionary."""
        if isinstance(obj, dict):
            return obj
        if hasattr(obj, '__dict__'):
            return obj.__dict__
        return {'value': obj}
    
    @staticmethod
    def serialize_value(value: Any) -> Any:
        """Serialize a single value."""
        if isinstance(value, (datetime, date)):
            return value.isoformat()
        elif isinstance(value, Decimal):
            return float(value)
        elif isinstance(value, UUID):
            return str(value)
        elif isinstance(value, dict):
            return {k: DataSerializer.serialize_value(v) for k, v in value.items()}
        elif isinstance(value, (list, tuple)):
            return [DataSerializer.serialize_value(v) for v in value]
        return value


class CustomJSONEncoder(json.JSONEncoder):
    """Custom JSON encoder for complex types."""
    
    def default(self, obj: Any) -> Any:
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        elif isinstance(obj, Decimal):
            return float(obj)
        elif isinstance(obj, UUID):
            return str(obj)
        elif hasattr(obj, '__dict__'):
            return obj.__dict__
        return super().default(obj)


def serialize_response(data: Any) -> Any:
    """Serialize response data."""
    return DataSerializer.serialize_value(data)
