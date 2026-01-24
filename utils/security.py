"""
Security Utilities
Encryption, hashing, and security-related functions
"""

import hashlib
import secrets
from typing import Tuple
import logging

logger = logging.getLogger(__name__)


class PasswordManager:
    """Handle password hashing and verification"""
    
    @staticmethod
    def hash_password(password: str, salt: str = None) -> Tuple[str, str]:
        """
        Hash password with salt
        
        Args:
            password: Plain text password
            salt: Optional salt (generated if not provided)
            
        Returns:
            Tuple of (hashed_password, salt)
        """
        if salt is None:
            salt = secrets.token_hex(32)
        
        # Use PBKDF2 for password hashing
        hash_obj = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            salt.encode('utf-8'),
            100000  # iterations
        )
        
        hashed = hash_obj.hex()
        return hashed, salt
    
    @staticmethod
    def verify_password(password: str, hashed: str, salt: str) -> bool:
        """
        Verify password against hash
        
        Args:
            password: Plain text password
            hashed: Stored hash
            salt: Stored salt
            
        Returns:
            True if password matches
        """
        new_hash, _ = PasswordManager.hash_password(password, salt)
        return new_hash == hashed
    
    @staticmethod
    def generate_secure_token(length: int = 32) -> str:
        """
        Generate secure random token
        
        Args:
            length: Token length in bytes
            
        Returns:
            Hex-encoded token
        """
        return secrets.token_hex(length)


class DataEncryption:
    """Handle data encryption and decryption (placeholder)"""
    
    @staticmethod
    def encrypt(data: str, key: str = None) -> str:
        """
        Encrypt data (placeholder implementation)
        
        Args:
            data: Data to encrypt
            key: Encryption key
            
        Returns:
            Encrypted data
        """
        logger.debug("Encrypting data")
        # Placeholder for actual encryption
        return data
    
    @staticmethod
    def decrypt(encrypted_data: str, key: str = None) -> str:
        """
        Decrypt data (placeholder implementation)
        
        Args:
            encrypted_data: Encrypted data
            key: Decryption key
            
        Returns:
            Decrypted data
        """
        logger.debug("Decrypting data")
        # Placeholder for actual decryption
        return encrypted_data


class SecurityHeaders:
    """Generate security headers for HTTP responses"""
    
    @staticmethod
    def get_security_headers() -> dict:
        """
        Get recommended security headers
        
        Returns:
            Dictionary of security headers
        """
        return {
            'X-Content-Type-Options': 'nosniff',
            'X-Frame-Options': 'DENY',
            'X-XSS-Protection': '1; mode=block',
            'Strict-Transport-Security': 'max-age=31536000; includeSubDomains',
            'Content-Security-Policy': "default-src 'self'",
            'Referrer-Policy': 'strict-origin-when-cross-origin'
        }


class InputSanitizer:
    """Sanitize user input to prevent attacks"""
    
    @staticmethod
    def sanitize_string(input_str: str) -> str:
        """
        Sanitize string input
        
        Args:
            input_str: Input string
            
        Returns:
            Sanitized string
        """
        if not isinstance(input_str, str):
            return ""
        
        # Remove dangerous characters
        dangerous_chars = ['<', '>', '"', "'", ';', '&']
        result = input_str
        for char in dangerous_chars:
            result = result.replace(char, '')
        
        return result.strip()
    
    @staticmethod
    def validate_file_upload(filename: str, allowed_extensions: list) -> bool:
        """
        Validate file upload
        
        Args:
            filename: Uploaded filename
            allowed_extensions: List of allowed extensions
            
        Returns:
            True if file is safe to upload
        """
        if not filename:
            return False
        
        ext = filename.rsplit('.', 1)[1].lower() if '.' in filename else ''
        return ext in allowed_extensions
