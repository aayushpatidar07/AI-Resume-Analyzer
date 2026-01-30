"""
Data Validation Schemas
Define and validate data schemas
"""

from typing import Dict, Any, List, Optional
from enum import Enum


class FieldType(Enum):
    """Data field types"""
    STRING = "string"
    INTEGER = "integer"
    FLOAT = "float"
    BOOLEAN = "boolean"
    EMAIL = "email"
    FILE = "file"
    LIST = "list"


class Schema:
    """Base schema class"""
    
    def __init__(self, name: str):
        self.name = name
        self.fields: Dict[str, Dict[str, Any]] = {}
    
    def add_field(self, field_name: str, field_type: FieldType,
                 required: bool = True, min_length: int = None,
                 max_length: int = None) -> 'Schema':
        """Add field to schema"""
        self.fields[field_name] = {
            'type': field_type,
            'required': required,
            'min_length': min_length,
            'max_length': max_length
        }
        return self
    
    def validate(self, data: Dict[str, Any]) -> tuple[bool, List[str]]:
        """Validate data against schema"""
        errors = []
        
        for field_name, field_config in self.fields.items():
            if field_config['required'] and field_name not in data:
                errors.append(f"Missing required field: {field_name}")
            
            if field_name in data:
                value = data[field_name]
                
                # Type validation
                if field_config['type'] == FieldType.STRING:
                    if not isinstance(value, str):
                        errors.append(f"{field_name} must be string")
                    
                    if field_config['min_length'] and len(value) < field_config['min_length']:
                        errors.append(f"{field_name} is too short")
                    
                    if field_config['max_length'] and len(value) > field_config['max_length']:
                        errors.append(f"{field_name} is too long")
        
        return len(errors) == 0, errors


class SchemaRegistry:
    """Registry for schemas"""
    
    _schemas: Dict[str, Schema] = {}
    
    @staticmethod
    def register_schema(schema: Schema) -> None:
        """Register a schema"""
        SchemaRegistry._schemas[schema.name] = schema
    
    @staticmethod
    def get_schema(schema_name: str) -> Optional[Schema]:
        """Get registered schema"""
        return SchemaRegistry._schemas.get(schema_name)
    
    @staticmethod
    def validate(schema_name: str, data: Dict[str, Any]) -> tuple[bool, List[str]]:
        """Validate data using registered schema"""
        schema = SchemaRegistry.get_schema(schema_name)
        if not schema:
            return False, [f"Schema not found: {schema_name}"]
        return schema.validate(data)


# Register common schemas
analysis_schema = Schema("analysis_request")
analysis_schema.add_field("resume", FieldType.FILE, required=True)
analysis_schema.add_field("job_description", FieldType.STRING, required=True, min_length=10)
SchemaRegistry.register_schema(analysis_schema)

user_schema = Schema("user_registration")
user_schema.add_field("email", FieldType.EMAIL, required=True)
user_schema.add_field("username", FieldType.STRING, required=True, min_length=3, max_length=50)
user_schema.add_field("password", FieldType.STRING, required=True, min_length=8)
SchemaRegistry.register_schema(user_schema)
