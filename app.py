"""
AI Resume Analyzer & Job Matcher
A Flask web application to analyze resumes and match them with job descriptions
via RESTful API.

Author: Aayush Patidar
Repository: https://github.com/aayushpatidar07/AI-Resume-Analyzer
Version: 1.0.0
"""

import os
import sys
import logging
import traceback
from datetime import datetime
from functools import lru_cache
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request, jsonify, redirect, url_for

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Import custom modules
from utils.resume_parser import ResumeParser
from utils.skill_extractor import SkillExtractor
from utils.matcher import SkillMatcher

# Configuration constants
MAX_FILE_SIZE = 16 * 1024 * 1024  # 16MB
MIN_JOB_DESC_LENGTH = 10
ALLOWED_EXTENSIONS = {'pdf'}
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')

# Flask Application Setup
app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = MAX_FILE_SIZE
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    """Check if file has allowed extension"""
    if not filename or '.' not in filename:
        return False
    return filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    """Home page route"""
    try:
        return render_template('index.html')
    except Exception as e:
        return f"Error loading home page: {str(e)}", 500


@app.route('/analyze', methods=['POST'])
def analyze():
    """
    Main analysis route
    Handles resume upload and job description submission
    """
    try:
        # Validate form data
        if 'resume' not in request.files:
            return jsonify({
                'success': False,
                'error': 'No resume file provided'
            }), 400
        
        if not request.form.get('job_description'):
            return jsonify({
                'success': False,
                'error': 'No job description provided'
            }), 400
        
        resume_file = request.files['resume']
        job_description = request.form.get('job_description').strip()
        
        # Validate file
        if resume_file.filename == '':
            return jsonify({
                'success': False,
                'error': 'No resume file selected'
            }), 400
        
        if not allowed_file(resume_file.filename):
            return jsonify({
                'success': False,
                'error': 'Only PDF files are allowed'
            }), 400
        
        if len(job_description) < MIN_JOB_DESC_LENGTH:
            return jsonify({
                'success': False,
                'error': f'Job description must be at least {MIN_JOB_DESC_LENGTH} characters'
            }), 400
        
        # Create uploads directory if it doesn't exist
        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
        
        # Save uploaded file with timestamp
        filename = secure_filename(resume_file.filename)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S_')
        filename = f"{timestamp}{filename}"
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        resume_file.save(file_path)
        
        # Step 1: Parse resume
        parse_result = ResumeParser.parse_resume(file_path)
        
        if not parse_result['success']:
            return jsonify({
                'success': False,
                'error': f"Failed to parse resume: {parse_result['error']}"
            }), 400
        
        resume_text = parse_result['cleaned_text']
        
        # Step 2: Extract skills from resume
        resume_skills = SkillExtractor.extract_from_resume(resume_text)
        
        # Step 3: Extract skills from job description
        job_text = job_description.lower()
        job_skills = SkillExtractor.extract_from_job_description(job_text)
        
        if not job_skills:
            return jsonify({
                'success': False,
                'error': 'No recognized skills found in job description'
            }), 400
        
        if not resume_skills:
            return jsonify({
                'success': False,
                'error': 'No recognized skills found in resume'
            }), 400
        
        # Step 4: Match resume with job
        match_result = SkillMatcher.match_resume(resume_skills, job_skills)
        
        # Step 5: Get match level
        match_level = SkillMatcher.get_match_level(match_result['match_percentage'])
        
        # Prepare response
        analysis_result = {
            'success': True,
            'match_percentage': match_result['match_percentage'],
            'match_level': match_level,
            'matched_skills': match_result['matched_skills'],
            'missing_skills': match_result['missing_skills'],
            'resume_skills_count': match_result['resume_skills_count'],
            'required_skills_count': match_result['required_skills_count'],
            'matched_count': match_result['matched_count'],
            'missing_count': match_result['missing_count']
        }
        
        # Clean up uploaded file
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
        except Exception as cleanup_error:
            logger.warning(f"Failed to remove temporary file {file_path}: {cleanup_error}")
        
        return jsonify(analysis_result)
    
    except Exception as e:
        # Log error for debugging
        logger.error(f"Error during analysis: {str(e)}", exc_info=True)
        
        return jsonify({
            'success': False,
            'error': 'An unexpected error occurred during analysis'
        }), 500


@app.route('/api/sample-data')
def sample_data():
    """
    API endpoint to provide sample data for testing
    """
    sample_job = """
    Senior Full Stack Developer
    
    Required Skills:
    - Python, JavaScript, React, Node.js
    - SQL, MongoDB, PostgreSQL
    - AWS, Docker, Kubernetes
    - REST APIs, Git, Agile
    
    Nice to have:
    - Machine Learning, TensorFlow
    - Microservices Architecture
    """
    
    return jsonify({
        'sample_job_description': sample_job
    })


@app.errorhandler(404)
def page_not_found(error):
    """Handle 404 errors"""
    return jsonify({
        'success': False,
        'error': 'Page not found'
    }), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({
        'success': False,
        'error': 'Internal server error'
    }), 500


@app.errorhandler(413)
def request_entity_too_large(error):
    """Handle file too large errors"""
    return jsonify({
        'success': False,
        'error': 'File size exceeds maximum limit (16MB)'
    }), 413


if __name__ == '__main__':
    # Create uploads directory
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    
    # Run Flask app
    logger.info("=" * 60)
    logger.info("AI Resume Analyzer & Job Matcher")
    logger.info("=" * 60)
    logger.info("Starting Flask development server...")
    logger.info("Navigate to: http://127.0.0.1:5000")
    logger.info("=" * 60)
    
    # Run Flask app (single invocation)
    logger.info("Starting Flask development server (debug=%s)", True)
    app.run(debug=True, host='127.0.0.1', port=5000)
