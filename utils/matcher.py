"""
Skill Matcher Module
Matches resume skills with job description requirements
"""

from typing import List, Dict, Tuple


class SkillMatcher:
    """
    Matches resume skills with job requirements
    """
    
    # Cache for normalized skill sets
    _skill_cache = {}
    
    @staticmethod
    def _normalize_skills(skills: List[str]) -> set:
        """Normalize skills to lowercase set for caching"""
        skill_tuple = tuple(sorted([s.lower() for s in skills]))
        if skill_tuple not in SkillMatcher._skill_cache:
            SkillMatcher._skill_cache[skill_tuple] = set(skill_tuple)
        return SkillMatcher._skill_cache[skill_tuple]
    
    @staticmethod
    def calculate_match_percentage(resume_skills: List[str], 
                                  job_skills: List[str],
                                  method: str = 'intersection') -> float:
        """
        Calculate match percentage between resume and job skills
        
        Args:
            resume_skills (List[str]): Skills found in resume
            job_skills (List[str]): Skills required for job
            method (str): Matching method ('intersection', 'jaccard', 'cosine')
            
        Returns:
            float: Match percentage (0-100)
        """
        if not job_skills:
            return 0.0
        
        # Use cached normalization
        resume_set = SkillMatcher._normalize_skills(resume_skills)
        job_set = SkillMatcher._normalize_skills(job_skills)
        
        # Calculate intersection (matched skills)
        matched = len(resume_set.intersection(job_set))
        total_required = len(job_set)
        
        # Calculate percentage
        match_percentage = (matched / total_required) * 100 if total_required > 0 else 0
        
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
            List[str]: Skills that match
        """
        resume_set = set(skill.lower() for skill in resume_skills)
        job_set = set(skill.lower() for skill in job_skills)
        
        matched = resume_set.intersection(job_set)
        return sorted(list(matched))
    
    @staticmethod
    def get_missing_skills(resume_skills: List[str], 
                          job_skills: List[str]) -> List[str]:
        """
        Get list of skills that are missing from resume
        
        Args:
            resume_skills (List[str]): Skills from resume
            job_skills (List[str]): Skills required for job
            
        Returns:
            List[str]: Skills that are missing
        """
        resume_set = set(skill.lower() for skill in resume_skills)
        job_set = set(skill.lower() for skill in job_skills)
        
        missing = job_set - resume_set
        return sorted(list(missing))
    
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
