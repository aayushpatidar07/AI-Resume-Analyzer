"""
Test Utilities
Helper functions and fixtures for testing
"""

import os
import tempfile
from typing import Generator, Tuple
from pathlib import Path


class TestDataGenerator:
    """Generate test data for testing"""
    
    @staticmethod
    def create_sample_resume_text() -> str:
        """Create sample resume text for testing"""
        return """
        John Doe
        Senior Software Engineer
        
        SKILLS
        - Python, JavaScript, React, Node.js
        - PostgreSQL, MongoDB, Redis
        - Docker, Kubernetes, AWS
        - REST APIs, GraphQL
        - Git, CI/CD, Jenkins
        
        EXPERIENCE
        Senior Developer at Tech Corp (2020-Present)
        - Led development of microservices using Python and FastAPI
        - Implemented Docker containerization
        - Managed Kubernetes clusters on AWS
        
        Developer at StartupXYZ (2018-2020)
        - Full-stack web development with React and Node.js
        - Database design with PostgreSQL and MongoDB
        - Implemented Redis caching
        """
    
    @staticmethod
    def create_sample_job_description() -> str:
        """Create sample job description for testing"""
        return """
        Senior Full Stack Developer
        
        Required Skills:
        - 5+ years with Python and JavaScript
        - React, Node.js, FastAPI experience
        - PostgreSQL, MongoDB
        - Docker and Kubernetes
        - AWS cloud services
        - REST APIs
        - Git and CI/CD
        
        Nice to have:
        - GraphQL experience
        - Redis caching
        - Microservices architecture
        """
    
    @staticmethod
    def create_temp_pdf_file() -> Generator[str, None, None]:
        """Create temporary PDF file for testing"""
        with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as f:
            temp_path = f.name
        try:
            yield temp_path
        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)


class TestFixtures:
    """Common test fixtures"""
    
    @staticmethod
    def get_test_upload_dir() -> str:
        """Get test uploads directory"""
        test_dir = 'test_uploads'
        os.makedirs(test_dir, exist_ok=True)
        return test_dir
    
    @staticmethod
    def cleanup_test_uploads() -> None:
        """Clean up test uploads directory"""
        import shutil
        test_dir = 'test_uploads'
        if os.path.exists(test_dir):
            shutil.rmtree(test_dir)
