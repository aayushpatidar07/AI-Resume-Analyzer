"""
Helpers Module
General utility helper functions
"""

import os
from typing import List, Dict, Any, Optional
from datetime import datetime


class FileHelper:
    """File handling utilities"""
    
    @staticmethod
    def ensure_directory_exists(path: str) -> str:
        """
        Create directory if it doesn't exist
        
        Args:
            path: Directory path
            
        Returns:
            Directory path
        """
        os.makedirs(path, exist_ok=True)
        return path
    
    @staticmethod
    def get_file_size(file_path: str) -> int:
        """
        Get file size in bytes
        
        Args:
            file_path: Path to file
            
        Returns:
            File size in bytes
        """
        return os.path.getsize(file_path)
    
    @staticmethod
    def format_file_size(size_bytes: int) -> str:
        """
        Format bytes to human-readable size
        
        Args:
            size_bytes: Size in bytes
            
        Returns:
            Formatted size string
        """
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size_bytes < 1024:
                return f"{size_bytes:.2f} {unit}"
            size_bytes /= 1024
        return f"{size_bytes:.2f} TB"


class DateTimeHelper:
    """DateTime handling utilities"""
    
    @staticmethod
    def get_timestamp() -> str:
        """
        Get current timestamp in ISO format
        
        Returns:
            ISO format timestamp
        """
        return datetime.now().isoformat()
    
    @staticmethod
    def format_datetime(dt: datetime, format_str: str = "%Y-%m-%d %H:%M:%S") -> str:
        """
        Format datetime object
        
        Args:
            dt: DateTime object
            format_str: Format string
            
        Returns:
            Formatted datetime string
        """
        return dt.strftime(format_str)


class ListHelper:
    """List/Collection handling utilities"""
    
    @staticmethod
    def remove_duplicates(items: List[Any]) -> List[Any]:
        """
        Remove duplicates while preserving order (optimized with dict.fromkeys)
        
        Args:
            items: List with potential duplicates
            
        Returns:
            List with duplicates removed
        """
        try:
            # Optimized: dict.fromkeys maintains insertion order (Python 3.7+)
            return list(dict.fromkeys(items))
        except TypeError:
            # Fallback for unhashable types
            seen = set()
            result = []
            for item in items:
                try:
                    if item not in seen:
                        seen.add(item)
                        result.append(item)
                except TypeError:
                    result.append(item)
            return result
    
    @staticmethod
    def flatten_list(nested_list: List[List[Any]]) -> List[Any]:
        """
        Flatten nested list (optimized for single-level nesting)
        
        Args:
            nested_list: Nested list structure
            
        Returns:
            Flattened list
        """
        result = []
        for item in nested_list:
            if isinstance(item, (list, tuple)):
                result.extend(ListHelper.flatten_list(item))
            else:
                result.append(item)
        return result
    
    @staticmethod
    def chunk_list(items: List[Any], chunk_size: int) -> List[List[Any]]:
        """
        Split list into chunks
        
        Args:
            items: List to chunk
            chunk_size: Size of each chunk
            
        Returns:
            List of chunks
        """
        return [items[i:i + chunk_size] for i in range(0, len(items), chunk_size)]


class DictHelper:
    """Dictionary handling utilities"""
    
    @staticmethod
    def merge_dicts(dict1: Dict, dict2: Dict) -> Dict:
        """
        Merge two dictionaries (optimized with dict unpacking)
        
        Args:
            dict1: First dictionary
            dict2: Second dictionary (takes precedence)
            
        Returns:
            Merged dictionary
        """
        # More Pythonic and efficient
        return {**dict1, **dict2}
    
    @staticmethod
    def get_nested(data: Dict, path: str, default: Any = None) -> Any:
        """
        Get nested dictionary value using dot notation
        
        Args:
            data: Dictionary
            path: Dot-separated path (e.g., 'user.profile.name')
            default: Default value if path not found
            
        Returns:
            Value at path or default
        """
        keys = path.split('.')
        value = data
        
        for key in keys:
            if isinstance(value, dict):
                value = value.get(key)
                if value is None:
                    return default
            else:
                return default
        
        return value
