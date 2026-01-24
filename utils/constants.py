"""
Constants Module
Application-wide constants and configuration values
"""

# File upload settings
MAX_FILE_SIZE = 16 * 1024 * 1024  # 16MB
ALLOWED_EXTENSIONS = {'pdf'}
UPLOAD_FOLDER = 'uploads'

# Text processing
MIN_JOB_DESCRIPTION_LENGTH = 10
MIN_SKILL_NAME_LENGTH = 2
MAX_SKILLS_TO_RETURN = None  # None = no limit

# Matching thresholds
EXCELLENT_MATCH_THRESHOLD = 80
GOOD_MATCH_THRESHOLD = 60
FAIR_MATCH_THRESHOLD = 40
POOR_MATCH_THRESHOLD = 0

# API settings
API_TIMEOUT = 30
MAX_RETRIES = 3
RETRY_DELAY = 1

# Logging
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
LOG_LEVEL = 'INFO'

# HTTP status codes
HTTP_OK = 200
HTTP_BAD_REQUEST = 400
HTTP_NOT_FOUND = 404
HTTP_SERVER_ERROR = 500

# Error messages
ERROR_NO_RESUME_FILE = 'No resume file provided'
ERROR_NO_JOB_DESCRIPTION = 'No job description provided'
ERROR_INVALID_FILE_TYPE = 'Only PDF files are allowed'
ERROR_RESUME_PARSE_FAILED = 'Failed to parse resume'
ERROR_NO_SKILLS_FOUND = 'No recognized skills found'
ERROR_UNEXPECTED = 'An unexpected error occurred'
