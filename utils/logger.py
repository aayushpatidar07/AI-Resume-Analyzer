"""
Logger Module
Centralized logging configuration and utilities
"""

import logging
import logging.handlers
import os
from typing import Optional


class LoggerSetup:
    """Setup and configure application-wide logging"""
    
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(LoggerSetup, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        self.logger = logging.getLogger('AI-Resume-Analyzer')
        self._configured = False
    
    def configure(self, 
                  level: int = logging.INFO,
                  log_file: Optional[str] = None) -> logging.Logger:
        """
        Configure logger with console and optional file handlers
        
        Args:
            level: Logging level (default: INFO)
            log_file: Path to log file (optional)
            
        Returns:
            Configured logger instance
        """
        if self._configured:
            return self.logger
        
        self.logger.setLevel(level)
        
        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)
        console_formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        console_handler.setFormatter(console_formatter)
        self.logger.addHandler(console_handler)
        
        # File handler (if specified)
        if log_file:
            os.makedirs(os.path.dirname(log_file) or '.', exist_ok=True)
            file_handler = logging.handlers.RotatingFileHandler(
                log_file,
                maxBytes=10485760,  # 10MB
                backupCount=5
            )
            file_handler.setLevel(level)
            file_formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            file_handler.setFormatter(file_formatter)
            self.logger.addHandler(file_handler)
        
        self._configured = True
        return self.logger
    
    def get_logger(self) -> logging.Logger:
        """Get the configured logger instance"""
        return self.logger


def get_logger(name: str) -> logging.Logger:
    """
    Get a logger instance with the given name
    
    Args:
        name: Logger name (typically __name__)
        
    Returns:
        Logger instance
    """
    return logging.getLogger(f'AI-Resume-Analyzer.{name}')
