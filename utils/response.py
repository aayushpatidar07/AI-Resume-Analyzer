"""
Response Module
Standardized response formatting for API endpoints
"""

from typing import Any, Dict, Optional, List


class ApiResponse:
    """Standardized API response formatter"""
    
    @staticmethod
    def success(data: Any = None, 
                message: str = "Success",
                status_code: int = 200) -> tuple:
        """
        Format successful API response
        
        Args:
            data: Response data payload
            message: Success message
            status_code: HTTP status code
            
        Returns:
            Tuple of (response_dict, status_code)
        """
        response = {
            'success': True,
            'message': message,
            'data': data,
            'status_code': status_code
        }
        return response, status_code
    
    @staticmethod
    def error(error_message: str,
              error_code: Optional[str] = None,
              status_code: int = 400,
              details: Optional[Dict] = None) -> tuple:
        """
        Format error API response
        
        Args:
            error_message: Error message
            error_code: Optional error code
            status_code: HTTP status code
            details: Optional additional error details
            
        Returns:
            Tuple of (response_dict, status_code)
        """
        response = {
            'success': False,
            'message': error_message,
            'error_code': error_code,
            'status_code': status_code
        }
        
        if details:
            response['details'] = details
        
        return response, status_code
    
    @staticmethod
    def paginated(items: List[Any],
                  total: int,
                  page: int = 1,
                  page_size: int = 10,
                  message: str = "Success") -> tuple:
        """
        Format paginated API response
        
        Args:
            items: List of items
            total: Total number of items
            page: Current page number
            page_size: Items per page
            message: Success message
            
        Returns:
            Tuple of (response_dict, status_code)
        """
        total_pages = (total + page_size - 1) // page_size
        
        response = {
            'success': True,
            'message': message,
            'data': items,
            'pagination': {
                'current_page': page,
                'page_size': page_size,
                'total_items': total,
                'total_pages': total_pages
            }
        }
        
        return response, 200
