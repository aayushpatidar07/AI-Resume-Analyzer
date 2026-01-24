"""
Resume Parser Module
Extracts text from PDF resume files
"""

import re
from typing import Dict, Any
from PyPDF2 import PdfReader


class ResumeParser:
    """
    Handles PDF resume file parsing and text extraction
    """
    
    @staticmethod
    def extract_text(file_path: str) -> str:
        """
        Extract text content from a PDF file
        
        Args:
            file_path (str): Path to the PDF file
            
        Returns:
            str: Extracted text from the PDF
            
        Raises:
            Exception: If file cannot be read or is not a valid PDF
        """
        try:
            text = ""
            pdf_reader = PdfReader(file_path)
            
            # Extract text from all pages
            for page_num, page in enumerate(pdf_reader.pages):
                text += page.extract_text()
                
            return text
        
        except Exception as e:
            raise Exception(f"Error reading PDF file: {str(e)}")
    
    @staticmethod
    def clean_text(text: str) -> str:
        """
        Clean and normalize extracted text
        
        Args:
            text (str): Raw extracted text
            
        Returns:
            str: Cleaned text
        """
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text)
        
        # Remove special characters but keep alphanumeric and common symbols
        text = re.sub(r'[^\w\s\.\-\+\#\@]', ' ', text)
        
        # Convert to lowercase
        text = text.lower()
        
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
