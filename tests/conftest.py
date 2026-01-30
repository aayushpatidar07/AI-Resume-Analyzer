"""
Testing Framework
Comprehensive testing utilities and fixtures
"""

import pytest
from typing import Generator, Any
import tempfile
import os


class TestConfig:
    """Test configuration"""
    TESTING = True
    DEBUG = True
    UPLOAD_FOLDER = 'test_uploads'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024


@pytest.fixture
def app():
    """Create app for testing"""
    from app import app
    app.config.update(TestConfig.__dict__)
    return app


@pytest.fixture
def client(app):
    """Create test client"""
    return app.test_client()


@pytest.fixture
def temp_file() -> Generator[str, None, None]:
    """Create temporary test file"""
    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as f:
        temp_path = f.name
    try:
        yield temp_path
    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)


@pytest.fixture
def sample_resume():
    """Sample resume text"""
    return """
    John Doe
    Senior Developer
    
    Skills: Python, JavaScript, React, Docker, Kubernetes
    Experience: 5+ years in full-stack development
    """


@pytest.fixture
def sample_job_description():
    """Sample job description"""
    return """
    Senior Full Stack Developer
    
    Required Skills:
    - Python, JavaScript, React
    - Docker, Kubernetes
    - AWS, CI/CD
    """


class TestHelpers:
    """Test helper functions"""
    
    @staticmethod
    def assert_success_response(response: Any) -> dict:
        """Assert successful API response"""
        assert response.status_code == 200
        data = response.get_json()
        assert data['success'] is True
        return data
    
    @staticmethod
    def assert_error_response(response: Any, status_code: int = 400) -> dict:
        """Assert error API response"""
        assert response.status_code == status_code
        data = response.get_json()
        assert data['success'] is False
        return data
