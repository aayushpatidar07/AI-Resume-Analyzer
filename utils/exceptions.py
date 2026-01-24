"""
Custom Exceptions Module
Application-specific exception classes
"""


class ResumeAnalyzerException(Exception):
    """Base exception class for the application"""
    pass


class ResumeParsError(ResumeAnalyzerException):
    """Exception raised when resume parsing fails"""
    pass


class SkillExtractionError(ResumeAnalyzerException):
    """Exception raised when skill extraction fails"""
    pass


class ValidationException(ResumeAnalyzerException):
    """Exception raised when validation fails"""
    pass


class FileHandlingError(ResumeAnalyzerException):
    """Exception raised when file operations fail"""
    pass


class MatchingError(ResumeAnalyzerException):
    """Exception raised when skill matching fails"""
    pass
