"""
Skill Extractor Module
Extracts technical skills from text using keyword and NLP-based approaches
"""

import re
from typing import List, Set


class SkillExtractor:
    """
    Extracts technical skills from resume and job description text
    """
    
    # Comprehensive skill database
    TECHNICAL_SKILLS = {
        # Programming Languages
        'python', 'java', 'javascript', 'typescript', 'c++', 'c#', 'php', 'ruby',
        'go', 'rust', 'kotlin', 'swift', 'r', 'matlab', 'perl', 'scala', 'groovy',
        'objective-c', 'dart', 'elixir', 'haskell', 'clojure', 'lua', 'vb', 'visual basic',
        
        # Web Development
        'html', 'css', 'react', 'vue', 'angular', 'flask', 'django', 'fastapi',
        'express', 'nodejs', 'node.js', 'asp.net', 'laravel', 'spring', 'spring boot',
        'wordpress', 'shopify', 'next.js', 'nuxt', 'svelte', 'jquery', 'bootstrap',
        'tailwind', 'material ui', 'webpack', 'gulp', 'grunt', 'npm', 'yarn', 'pnpm',
        
        # Mobile Development
        'android', 'ios', 'react native', 'flutter', 'xamarin', 'swift',
        
        # Databases
        'sql', 'mysql', 'postgresql', 'mongodb', 'redis', 'sqlite', 'oracle',
        'elasticsearch', 'cassandra', 'dynamodb', 'firebase', 'couchdb',
        'mariadb', 'memcached', 'neo4j', 'influxdb',
        
        # Cloud & DevOps
        'aws', 'azure', 'gcp', 'docker', 'kubernetes', 'jenkins', 'gitlab', 'github',
        'ci/cd', 'terraform', 'ansible', 'puppet', 'chef', 'vagrant', 'heroku',
        'aws lambda', 'ec2', 's3', 'rds', 'cloudwatch', 'cloudformation',
        
        # Data Science & ML
        'machine learning', 'ml', 'deep learning', 'tensorflow', 'pytorch', 'keras',
        'scikit-learn', 'pandas', 'numpy', 'matplotlib', 'seaborn', 'jupyter',
        'nltk', 'spacy', 'computer vision', 'nlp', 'neural networks', 'opencv',
        'xgboost', 'lightgbm', 'catboost',
        
        # Big Data
        'spark', 'hadoop', 'hive', 'pig', 'mapreduce', 'kafka', 'rabbitmq',
        'flink', 'storm', 'scala', 'airflow',
        
        # Version Control
        'git', 'svn', 'mercurial', 'bitbucket',
        
        # Testing
        'junit', 'pytest', 'unittest', 'mocha', 'jest', 'selenium', 'cypress',
        'testng', 'rspec', 'qunit', 'karma', 'robotframework',
        
        # APIs & Services
        'rest', 'restful', 'graphql', 'soap', 'microservices', 'api',
        'grpc', 'websocket', 'openapi', 'swagger',
        
        # Agile & Collaboration
        'agile', 'scrum', 'kanban', 'jira', 'asana', 'trello', 'slack',
        'confluence', 'git', 'scrum master',
        
        # Other Tools & Frameworks
        'linux', 'unix', 'windows', 'macos', 'bash', 'shell', 'powershell',
        'apache', 'nginx', 'iis', 'tomcat', 'gunicorn', 'uwsgi',
        'graphene', 'marshmallow', 'sqlalchemy', 'orm', 'soap',
        'security', 'ssl', 'oauth', 'jwt', 'authentication', 'encryption'
    }
    
    @staticmethod
    def extract_keywords(text: str) -> Set[str]:
        """
        Extract skills from text using keyword matching
        
        Args:
            text (str): Cleaned text to extract skills from
            
        Returns:
            Set[str]: Set of extracted skills
        """
        text_lower = text.lower()
        extracted_skills = set()
        
        for skill in SkillExtractor.TECHNICAL_SKILLS:
            # Use word boundaries to match whole skills only
            pattern = r'\b' + re.escape(skill) + r'\b'
            if re.search(pattern, text_lower):
                extracted_skills.add(skill)
        
        return extracted_skills
    
    @staticmethod
    def extract_skills(text: str) -> List[str]:
        """
        Extract skills from text using keyword matching approach
        
        Args:
            text (str): Text to extract skills from
            
        Returns:
            List[str]: List of extracted skills
        """
        skills = SkillExtractor.extract_keywords(text)
        # Return sorted list for consistency
        return sorted(list(skills))
    
    @staticmethod
    def extract_from_resume(resume_text: str) -> List[str]:
        """
        Extract skills specifically from resume text
        
        Args:
            resume_text (str): Cleaned resume text
            
        Returns:
            List[str]: List of skills found in resume
        """
        return SkillExtractor.extract_skills(resume_text)
    
    @staticmethod
    def extract_from_job_description(job_text: str) -> List[str]:
        """
        Extract required skills from job description
        
        Args:
            job_text (str): Cleaned job description text
            
        Returns:
            List[str]: List of required skills for the job
        """
        return SkillExtractor.extract_skills(job_text)
