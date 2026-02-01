"""
Resume Parser Module
Extracts text from PDF resume files
"""

import re
from typing import Dict, Any, Tuple
from PyPDF2 import PdfReader


class ResumeParser:
    """
    Handles PDF resume file parsing and text extraction
    """
    
    # Configuration for text cleaning
    PRESERVE_SYMBOLS = {'.', '-', '+', '#', '@', ':', ',', '(', ')'}
    MIN_WORD_LENGTH = 2
    
    @staticmethod
    def extract_text(file_path: str) -> Tuple[str, int]:
        """
        Extract text content from a PDF file
        
        Args:
            file_path (str): Path to the PDF file
            
        Returns:
            Tuple of (extracted_text, page_count)
            
        Raises:
            Exception: If file cannot be read or is not a valid PDF
        """
        try:
            text = ""
            pdf_reader = PdfReader(file_path)
            page_count = len(pdf_reader.pages)
            
            # Extract text from all pages
            for page_num, page in enumerate(pdf_reader.pages):
                text += page.extract_text()
                
            return text, page_count
        
        except Exception as e:
            raise Exception(f"Error reading PDF file: {str(e)}")
    
    @staticmethod
    def clean_text(text: str, preserve_formatting: bool = False) -> str:
        """
        Clean and normalize extracted text with advanced options
        
        Args:
            text (str): Raw extracted text
            preserve_formatting (bool): Preserve line breaks and structure
            
        Returns:
            str: Cleaned text
        """
        if preserve_formatting:
            # Keep line structure but clean each line
            lines = text.split('\n')
            cleaned_lines = [ResumeParser._clean_line(line) for line in lines]
            return '\n'.join(cleaned_lines).strip()
        
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text)
        
        # Remove special characters but keep configured symbols
        text = ResumeParser._clean_line(text)
        
        # Convert to lowercase
        text = text.lower()
        
        return text.strip()
    
    @staticmethod
    def _clean_line(line: str) -> str:
        """Clean a single line while preserving configured symbols"""
        # Build regex pattern
        preserve_pattern = ''.join(re.escape(s) for s in ResumeParser.PRESERVE_SYMBOLS)
        pattern = f'[^\\w\\s{preserve_pattern}]'
        return re.sub(pattern, ' ', line)
    
    @staticmethod
    def parse_resume(file_path: str, preserve_formatting: bool = False) -> Dict[str, Any]:
        """
        Complete resume parsing pipeline
        
        Args:
            file_path (str): Path to the PDF file
            preserve_formatting (bool): Preserve text structure
            
        Returns:
            dict: Dictionary with parsing results including metadata
        """
        try:
            raw_text, page_count = ResumeParser.extract_text(file_path)
            cleaned_text = ResumeParser.clean_text(raw_text, preserve_formatting)
            
            return {
                'success': True,
                'raw_text': raw_text,
                'cleaned_text': cleaned_text,
                'page_count': page_count,
                'text_length': len(cleaned_text),
                'error': None
            }
        
        except Exception as e:
            return {
                'success': False,
                'raw_text': '',
                'cleaned_text': '',
                'page_count': 0,
                'text_length': 0,
                'error': str(e)
            }
