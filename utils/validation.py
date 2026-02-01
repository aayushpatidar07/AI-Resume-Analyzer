"""
Validation Module
Input validation and data validation utilities
"""

from typing import Any, List, Tuple
import re


class ValidationError(Exception):
    """Custom exception for validation errors"""
    pass


class Validator:
    """Utility class for input validation"""
    
    # Validation patterns
    PATTERNS = {
        'email': r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
        'url': r'^https?://[^\s/$.?#].[^\s]*$',
        'job_title': r'^[a-zA-Z0-9\s\-.,&()]+$',
        'alphanumeric': r'^[a-zA-Z0-9\s]+$'
    }
    
    @staticmethod
    def validate_string(value: Any, 
                       min_length: int = 0,
                       max_length: int = None,
                       field_name: str = "field",
                       pattern: str = None) -> str:
        """
        Validate string input
        
        Args:
            value: Value to validate
            min_length: Minimum string length
            max_length: Maximum string length (None = no limit)
            field_name: Field name for error messages
            pattern: Optional regex pattern to validate against
            
        Returns:
            Validated string
            
        Raises:
            ValidationError: If validation fails
        """
        if not isinstance(value, str):
            raise ValidationError(f"{field_name} must be a string")
        
        if len(value) < min_length:
            raise ValidationError(
                f"{field_name} must be at least {min_length} characters"
            )
        
        if max_length and len(value) > max_length:
            raise ValidationError(
                f"{field_name} must not exceed {max_length} characters"
            )
        
        if pattern and pattern in Validator.PATTERNS:
            if not re.match(Validator.PATTERNS[pattern], value):
                raise ValidationError(
                    f"{field_name} format is invalid"
                )
        
        return value.strip()
    
    @staticmethod
    def validate_file_extension(filename: str, 
                               allowed_extensions: List[str]) -> str:
        """
        Validate file extension
        
        Args:
            filename: Name of the file
            allowed_extensions: List of allowed extensions
            
        Returns:
            File extension if valid
            
        Raises:
            ValidationError: If extension not allowed
        """
        if '.' not in filename:
            raise ValidationError("File must have an extension")
        
        ext = filename.rsplit('.', 1)[1].lower()
        
        if ext not in allowed_extensions:
            raise ValidationError(
                f"File type .{ext} not allowed. "
                f"Allowed types: {', '.join(allowed_extensions)}"
            )
        
        return ext
    
    @staticmethod
    def validate_email(email: str) -> str:
        """
        Validate email format
        
        Args:
            email: Email address to validate
            
        Returns:
            Valid email address
            
        Raises:
            ValidationError: If email format invalid
        """
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        
        if not re.match(pattern, email):
            raise ValidationError("Invalid email format")
        
        return email
    
    @staticmethod
    def validate_skills_list(skills: List[str]) -> List[str]:
        """
        Validate and clean skills list
        
        Args:
            skills: List of skills
            
        Returns:
            Cleaned and validated skills list
            
        Raises:
            ValidationError: If validation fails
        """
        if not isinstance(skills, list):
            raise ValidationError("Skills must be a list")
        
        if len(skills) == 0:
            raise ValidationError("Skills list cannot be empty")
        
        cleaned = []
        for skill in skills:
            if not isinstance(skill, str):
                raise ValidationError(f"Skill must be string: {skill}")
            
            cleaned_skill = skill.strip().lower()
            if cleaned_skill:
                cleaned.append(cleaned_skill)
        
        return cleaned
