""" 
Resume Parser Module
Extracts text from PDF resume files with optimized performance
"""

import re
from typing import Dict, Any, List
from PyPDF2 import PdfReader
import logging

logger = logging.getLogger(__name__)


class ResumeParser:
    """
    Handles PDF resume file parsing and text extraction
    """
    
    @staticmethod
    def extract_text(file_path: str) -> str:
        """
        Extract text content from a PDF file with optimized performance
        
        Args:
            file_path (str): Path to the PDF file
            
        Returns:
            str: Extracted text from the PDF
            
        Raises:
            Exception: If file cannot be read or is not a valid PDF
        """
        try:
            pdf_reader = PdfReader(file_path)
            
            # Use list comprehension for better performance
            text_pages = [page.extract_text() or '' for page in pdf_reader.pages]
            text = ''.join(text_pages)
            
            if not text.strip():
                raise Exception("PDF appears to be empty or text extraction failed")
                
            return text
        
        except Exception as e:
            logger.error(f"Error reading PDF file {file_path}: {str(e)}")
            raise Exception(f"Error reading PDF file: {str(e)}")
    
    @staticmethod
    def clean_text(text: str) -> str:
        """
        Clean and normalize extracted text with optimized regex
        
        Args:
            text (str): Raw extracted text
            
        Returns:
            str: Cleaned text
        """
        if not text:
            return ""
        
        # Convert to lowercase first
        text = text.lower()
        
        # Remove extra whitespace (optimized)
        text = re.sub(r'\s+', ' ', text)
        
        # Remove special characters but keep alphanumeric and common symbols
        text = re.sub(r'[^\w\s\.\-\+\#\@]', ' ', text)
        
        # Remove extra spaces created by character removal
        text = re.sub(r'\s+', ' ', text)
        
        return text.strip()
    
    @staticmethod
    def parse_resume(file_path: str) -> Dict[str, Any]:
        """
        Complete resume parsing pipeline
        
        Args:
            file_path (str): Path to the PDF file
            
        Returns:
            dict: Dictionary with raw and cleaned text
        """
        try:
            raw_text = ResumeParser.extract_text(file_path)
            cleaned_text = ResumeParser.clean_text(raw_text)
            
            return {
                'success': True,
                'raw_text': raw_text,
                'cleaned_text': cleaned_text,
                'error': None
            }
        
        except Exception as e:
            return {
                'success': False,
                'raw_text': '',
                'cleaned_text': '',
                'error': str(e)
            }
