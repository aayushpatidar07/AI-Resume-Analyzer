"""
Error Handler Middleware
Centralized error handling for the application
"""

from typing import Tuple, Dict, Any
import logging

logger = logging.getLogger(__name__)


class ErrorHandler:
    """Centralized error handling"""
    
    ERROR_MESSAGES = {
        'FILE_NOT_FOUND': 'Resume file not found',
        'INVALID_PDF': 'Invalid PDF file format',
        'NO_TEXT_EXTRACTED': 'Could not extract text from resume',
        'NO_SKILLS_FOUND': 'No skills detected in the provided documents',
        'INVALID_INPUT': 'Invalid input provided',
        'FILE_TOO_LARGE': 'File size exceeds maximum limit',
        'PROCESSING_ERROR': 'Error during processing',
        'UNAUTHORIZED': 'Unauthorized access',
        'NOT_FOUND': 'Resource not found',
        'SERVER_ERROR': 'Internal server error',
        'VALIDATION_ERROR': 'Validation failed',
        'TIMEOUT_ERROR': 'Request timeout',
        'RATE_LIMIT_ERROR': 'Rate limit exceeded'
    }
    
    # HTTP status code mapping
    STATUS_CODES = {
        'FILE_NOT_FOUND': 404,
        'INVALID_PDF': 400,
        'NO_TEXT_EXTRACTED': 422,
        'NO_SKILLS_FOUND': 204,
        'INVALID_INPUT': 400,
        'FILE_TOO_LARGE': 413,
        'PROCESSING_ERROR': 500,
        'UNAUTHORIZED': 401,
        'NOT_FOUND': 404,
        'SERVER_ERROR': 500,
        'VALIDATION_ERROR': 422,
        'TIMEOUT_ERROR': 504,
        'RATE_LIMIT_ERROR': 429
    }
    
    @staticmethod
    def handle_error(error_code: str, 
                    status_code: int = 400,
                    additional_info: Dict[str, Any] = None) -> Tuple[Dict, int]:
        """
        Handle error with standardized response
        
        Args:
            error_code: Error code key
            status_code: HTTP status code
            additional_info: Additional error information
            
        Returns:
            Tuple of (error_response, status_code)
        """
        message = ErrorHandler.ERROR_MESSAGES.get(
            error_code, 
            'An unexpected error occurred'
        )
        
        response = {
            'success': False,
            'error_code': error_code,
            'message': message,
            'details': additional_info or {}
        }
        
        logger.error(f"Error {error_code}: {message}")
        return response, status_code
    
    @staticmethod
    def handle_exception(exception: Exception, 
                        error_code: str = 'SERVER_ERROR',
                        status_code: int = 500) -> Tuple[Dict, int]:
        """
        Handle exception
        
        Args:
            exception: Exception object
            error_code: Error code
            status_code: HTTP status code
            
        Returns:
            Tuple of (error_response, status_code)
        """
        logger.exception(f"Exception: {str(exception)}")
        
        response = {
            'success': False,
            'error_code': error_code,
            'message': ErrorHandler.ERROR_MESSAGES.get(
                error_code,
                'An unexpected error occurred'
            ),
            'details': {'exception': str(exception)}
        }
        
        return response, status_code
