"""
Database Models (ORM Setup Ready)
Prepared for future database integration
"""

from datetime import datetime
from typing import Optional, List


class BaseModel:
    """Base model class with common attributes"""
    
    def __init__(self):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def to_dict(self) -> dict:
        """Convert model to dictionary"""
        raise NotImplementedError


class User(BaseModel):
    """User model for future authentication"""
    
    def __init__(self, email: str, username: str, password_hash: Optional[str] = None):
        super().__init__()
        self.id = None
        self.email = email
        self.username = username
        self.password_hash = password_hash
        self.is_active = True
    
    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'email': self.email,
            'username': self.username,
            'is_active': self.is_active,
            'created_at': self.created_at.isoformat()
        }


class AnalysisResult(BaseModel):
    """Analysis result model for storing past analyses"""
    
    def __init__(self, 
                 user_id: Optional[int] = None,
                 resume_filename: str = "",
                 match_percentage: float = 0.0,
                 match_level: str = ""):
        super().__init__()
        self.id = None
        self.user_id = user_id
        self.resume_filename = resume_filename
        self.match_percentage = match_percentage
        self.match_level = match_level
        self.matched_skills: List[str] = []
        self.missing_skills: List[str] = []
    
    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'user_id': self.user_id,
            'resume_filename': self.resume_filename,
            'match_percentage': self.match_percentage,
            'match_level': self.match_level,
            'matched_skills': self.matched_skills,
            'missing_skills': self.missing_skills,
            'created_at': self.created_at.isoformat()
        }


class Skill(BaseModel):
    """Skill model for skill database"""
    
    def __init__(self, name: str, category: str = ""):
        super().__init__()
        self.id = None
        self.name = name
        self.category = category
        self.popularity_score = 0.0
    
    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'popularity_score': self.popularity_score
        }
