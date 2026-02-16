"""
Skill Matcher Module
Matches resume skills with job description requirements using optimized algorithms
"""

from typing import List, Dict, Tuple, Set
from functools import lru_cache


class SkillMatcher:
    """
    Matches resume skills with job requirements
    """
    
    @staticmethod
    def calculate_match_percentage(resume_skills: List[str], 
                                  job_skills: List[str]) -> float:
        """
        Calculate match percentage between resume and job skills with optimization
        
        Args:
            resume_skills (List[str]): Skills found in resume
            job_skills (List[str]): Skills required for job
            
        Returns:
            float: Match percentage (0-100)
        """
        if not job_skills:
            return 0.0
        
        if not resume_skills:
            return 0.0
        
        # Convert to sets for O(1) lookup - more efficient
        resume_set = {skill.lower() for skill in resume_skills}
        job_set = {skill.lower() for skill in job_skills}
        
        # Calculate intersection (matched skills)
        matched = len(resume_set & job_set)
        total_required = len(job_set)
        
        # Calculate percentage
        match_percentage = (matched / total_required) * 100
        
        return round(match_percentage, 2)
    
    @staticmethod
    def get_matched_skills(resume_skills: List[str], 
                          job_skills: List[str]) -> List[str]:
        """
        Get list of skills that match between resume and job
        
        Args:
            resume_skills (List[str]): Skills from resume
            job_skills (List[str]): Skills required for job
            
        Returns:
            List[str]: Sorted list of matched skills
        """
        resume_set = {skill.lower() for skill in resume_skills}
        job_set = {skill.lower() for skill in job_skills}
        
        # Use & operator for intersection (more Pythonic)
        matched = resume_set & job_set
        return sorted(matched)
    
    @staticmethod
    def get_missing_skills(resume_skills: List[str], 
                          job_skills: List[str]) -> List[str]:
        """
        Get list of skills that are missing from resume
        
        Args:
            resume_skills (List[str]): Skills from resume
            job_skills (List[str]): Skills required for job
            
        Returns:
            List[str]: Sorted list of missing skills
        """
        resume_set = {skill.lower() for skill in resume_skills}
        job_set = {skill.lower() for skill in job_skills}
        
        # Use - operator for difference (more Pythonic)
        missing = job_set - resume_set
        return sorted(missing)
    
    @staticmethod
    def match_resume(resume_skills: List[str], 
                    job_skills: List[str]) -> Dict:
        """
        Complete matching analysis between resume and job
        
        Args:
            resume_skills (List[str]): Skills from resume
            job_skills (List[str]): Skills required for job
            
        Returns:
            Dict: Complete matching analysis
        """
        matched_skills = SkillMatcher.get_matched_skills(resume_skills, job_skills)
        missing_skills = SkillMatcher.get_missing_skills(resume_skills, job_skills)
        match_percentage = SkillMatcher.calculate_match_percentage(
            resume_skills, job_skills
        )
        
        return {
            'match_percentage': match_percentage,
            'matched_skills': matched_skills,
            'missing_skills': missing_skills,
            'resume_skills_count': len(resume_skills),
            'required_skills_count': len(job_skills),
            'matched_count': len(matched_skills),
            'missing_count': len(missing_skills)
        }
    
    @staticmethod
    def get_match_level(percentage: float) -> str:
        """
        Get match level description based on percentage
        
        Args:
            percentage (float): Match percentage
            
        Returns:
            str: Match level description
        """
        if percentage >= 80:
            return "Excellent Match"
        elif percentage >= 60:
            return "Good Match"
        elif percentage >= 40:
            return "Fair Match"
        elif percentage >= 20:
            return "Poor Match"
        else:
            return "Very Poor Match"
